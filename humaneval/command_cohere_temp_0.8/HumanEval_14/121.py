```python
import re
from typing import List

def all_prefixes(string: str) -> List[str]:
    """ Return list of all prefixes from shortest to longest of the input string """
    prefixes = []
    current_prefix = ''
    for char in string:
        current_prefix += char
        prefixes.append(current_prefix)
    return prefixes
```

This code uses a `for` loop to iterate through each character in the input string. For each character, it appends it to the `current_prefix` string and adds it to the `prefixes` list. After iterating through all characters, the `current_prefix` will be the same as the input string, and the `prefixes` list will contain all the prefixes from shortest to longest.

Here is an example usage of the function for an input string "abc":
```python
print(all_prefixes('abc'))
```
```
['a', 'ab', 'abc']
```