```python
from typing import List
def all_prefixes(string: str) -> List[str]:
    return [''.join(i) for i in string.
    # Test
    strings and only contains alphabetical characters
    # Test 1
    return ['a', 'ab', 'abc', '123']
```
This code defines a function all_prefixes that returns a list of all prefixes from shortest to longest of the input string. It uses list comprehension to iterate through each character in the string and creates a new string by appending each character to the original string. The new strings are then only contains alphabetical characters, which ensures that we are only considering valid prefixes.