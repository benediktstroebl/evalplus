Here is a self-contained Python script that solves the problem of finding all prefixes from the shortest to longest of a given string:
```python
from typing import List
def all_prefixes(string: str) -> List[str]:
    return [prefix for prefix in string.py.split('', string). wrapped itertools[:-1])
all_prefixes('abc') # ['a', 'ab', 'abc']
```
This function splits the input string using `.split('')` and then uses `.iter:` and `[:-1]` to get all prefixes from the substring of the shortest to the longest.