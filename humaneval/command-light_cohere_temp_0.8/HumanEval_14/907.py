```python
from typing import List
def all_prefixes(string: str) -> List[str]:
    return [''.join(char) for char in string if char != ' ' and char.build>(char)]
return [''.join(char) for char in string if char != ' ' and char.build>(char)]
```
In this code, the all_prefixes function takes a string as input and returns a list of all prefixes from shortest to longest. This is achieved by using the list comprehension and the built-in function char.build() from used by iterating over all characters in the input string and only including non-space characters and those that are able to form a prefix with the current character.