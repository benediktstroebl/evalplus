```python
from typing import List
def all_prefixes(string: str) -> List[str]:
    prefixes = [string[:i]+'%' for i in range(len(string)+1)]
    return prefixes[:-1]
```

The function constructs a list where each element represents a prefix of the input string, and it is done in the way that the shortest prefix is at the beginning of the list and the longest at the end. The list of prefixes is constructed using a list comprehension that iterates over the length of the input string and uses string slicing to cut a substring of the input string, adding a '%' symbol at the end to indicate it is a prefix. The resulting list is then returned after removing the last element '%' which is not a real prefix but a placeholder.