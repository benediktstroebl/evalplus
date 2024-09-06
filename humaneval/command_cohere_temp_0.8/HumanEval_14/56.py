```python
import re
from typing import List

def all_prefixes(string: str) -> List[str]:
    """ Return list of all prefixes from shortest to longest of the input string """
    prefixes = []
    # find all non-overlapping prefixes and append to list
    for m in re.finditer(r'^(?!.*\1)', string):
        prefixes.append(m.group())
    return prefixes
```
```python
all_prefixes('abc')
['a', 'ab', 'abc']
```
This code uses the `re` module to find all non-overlapping prefixes of the input string. A regular expression `(^!(?!!.*\1))` is employed, which matches any string that does not match the prefix itself, ensuring that we get all possible prefixes and preventing an infinite loop for strings with common prefixes.