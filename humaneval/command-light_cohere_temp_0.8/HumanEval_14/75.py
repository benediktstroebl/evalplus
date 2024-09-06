Here is a self-contained Python function that solves the problem of finding all prefixes of a given string:
```python
from typing import List
def all_prefixes(string: str) -> List[str]:
    return [''.join([ch for ch in c if c != '']) for c in string.
    # Using the old-efficiently, by converting the string to a list of characters
    # and then using list comprehensions
```
This function takes a string as input and returns a list of all prefixes from shortest to longest of the input string.