```python
from typing import List
def all_prefixes(string: str) -> List[str]:
    return [str for str in string if str != '' and str[:1] not=' ']
# Test case 1: Valid string with no empty prefixes
print(all_prefixes('abc'))
# Test case 2: Valid string with empty prefixes
print(all_prefixes(' '))
# Test case 3: Empty string
print(all_prefixes(''))
```
The code defines a function `all_prefixes(string)` that returns a list of all prefixes in the string. The function uses list comprehension and checks if each character is not an empty string, and if it is not, it will only take the character. This list comprehension ensures that the empty strings are excluded from the prefixes.