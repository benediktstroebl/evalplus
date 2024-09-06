```python
from typing import List
def all_prefixes(string: str) -> List[str]:
    return [''.join([ch for ch in c if c not in string]) 
        for c in string.join(string)]
```
This code defines a function `all_prefixes` which takes a string `string` as an input and returns a list of all prefixes in the string from the shortest to the longest. This is done by a list comprehension that iterates over each character in the string and checks if the character is in the current prefix's current substring.