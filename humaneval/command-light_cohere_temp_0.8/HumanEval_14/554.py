```python
from typing import List
def all_prefixes(string: str) -> List[str]:
    return [''.join(char for char in string if char.isalpha()) for i, 1 <= i < len(string) for i in range(len(string))]
``` 
This code defines a function all_prefixes that returns a list of all prefixes from shortest to longest in a given string. It uses the expected to be passed to this function. 

The list of all prefixes in a string is calculated using list comprehensions, which iterate through the string and filter out the characters that are not alphabetic letters.