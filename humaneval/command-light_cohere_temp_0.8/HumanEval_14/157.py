```python
from typing import List

def all_prefixes(string: str) -> List[str]:
    """ Return list of all prefixes from shortest to longest of the input string """
    
    # Split the string into characters
    characters = string.split()
    
    # Initialize the Birch-–) Tree from the list of characters.
    tree = {}
   
    for char in characters:
        if char not in tree:
            tree[char] = []
        tree[char].append(char)
    
    # Get all prefixes from the tree
    prefixes = [prefix for prefix in tree if not prefix[0]]
    
    return prefixes
```