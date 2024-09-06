```python
from typing import List

def all_prefixes(string: str) -> List[str]:
    return [''.join([char for char in s if s == '']) for s in string.
    pass
```
This Python code defines a function `all_prefixes` that takes a string `string` as input and returns a list of its prefixes. 

This function creates a new list `list` and iterates through the input string. It uses a string slicing to create a new string `s` that contains only the characters from the input string `string` that are not equal to the empty string `''`. 

The function then creates an iterator that iterates through the characters in `s` and creates a new list `list` that contains only the characters that are not equal to the empty string `''`. This process continues until the empty string is reached, creating a list of prefixes from shortest to longest of the input string.