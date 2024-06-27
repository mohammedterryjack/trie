# trie
turn a list of labels into a tree

["example label 1", "example label 2", "another label )", "another label again"]

{
  "example label": {
    "1": {},
    "2": {}
  },
  "another label": {
    ")": {},
    "again": {}
  }
}

                  ┌1
    ┌example label┤ 
    │             └2
JSON┤               
    │             ┌)
    └another label┤ 
                  └again
