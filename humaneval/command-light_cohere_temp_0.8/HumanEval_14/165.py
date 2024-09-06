```python
from typing import List
def all_prefixes(string: str) -> List[str]:
    return ["".join(char) for char in string if char != '']
```

This function employs a list comprehension to generate an array of prefixes, where each prefix is a character from the input string if that character is not an underscore. 

Note: this is a self-contained solution and does not require external modules or functions.