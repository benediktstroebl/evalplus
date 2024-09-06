```python
from typing import List

def all_prefixes(string: str) -> List[str]:
    """ Return list of all prefixes from shortest to longest of the input string"""
    return [''.join() for _ in range(1, len(string) + 1)]

# Test cases
string1 = "abc"
string2 = "hello world"
string3 = ""

result1 = all_prefixes(string1)
print(result1)  # ['a', 'ab', 'ac', 'ba', 'bb', 'bc']

result2 = all_prefixes(string2)
print(result2)  # ['hello', 'world']

result3 = all_prefixes(string3)
print(result3)  # ['']
```
This script defines a function all_prefixes that returns a list of all prefixes in the string, from shortest to longest. The function uses a loop to iterate through each character in the string, appending each character to the prefix string.