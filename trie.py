from string import punctuation
from PrettyPrint import PrettyPrintTree
from json import dumps

def pad_punctuation(text:str) -> str:
    return text.translate(str.maketrans({key: " {0} ".format(key) for key in punctuation}))

def make_trie(names:list[str]) -> dict:
    root = dict()
    for name in names:
        current_dict = root
        for word in name.split():
            current_dict = current_dict.setdefault(word, {})
    return root

def simplify_trie(trie:dict) -> dict:
    simplified_trie = {}
    nodes = [([],trie)]    
    while any(nodes):
        parents,node = nodes.pop(0)    
        current_dict = simplified_trie
        for parent in parents:    
            current_dict = current_dict[parent]
        for name,children in node.items():    
            if len(children)==1:
                for childname,child in children.items():    
                    nodes.append((parents,{f"{name} {childname}":child}))
            else:    
                current_dict[name] = {}
                nodes.extend([
                    (parents+[name], {k:v}) for k,v in children.items()
                ])
    return simplified_trie

def list_to_trie(labels:list[str]) -> dict:
    labels = [pad_punctuation(text=label) for label in labels]
    trie = make_trie(labels)
    return simplify_trie(trie=trie)

pprint_tree = PrettyPrintTree(orientation=PrettyPrintTree.Horizontal, color='')
tree = list_to_trie(labels=["example label", "example label 2", "another label", "another label again"])
repr = pprint_tree.print_json(tree, return_instead_of_print=True)
with open('tree.txt','w') as f:
    f.write(repr)
with open('tree.json', 'w') as f:
    f.write(dumps(tree,indent=2))
pprint_tree.print_json(tree)
