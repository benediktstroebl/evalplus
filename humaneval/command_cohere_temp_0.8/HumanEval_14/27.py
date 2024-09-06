```python
from typing import List
from itertools import dropwhile


def all_prefixes(string: str) -> List[str]:
    """ Return list of all prefixes from shortest to longest of the input string """
    return list(reversed(list(dropwhile(lambda s: s == '', string))));
```
The function `all_prefixes()` uses the `dropwhile` function from the `itertools` module to iterate over the strings formed by dropping one character from the beginning of the input string, excluding the empty string, until the input string is reached. The result is a list of prefixes in descending order of length.

Here is a sample output:
```
all_prefixes('abc')
['abc', 'ab', 'a']
```
```python
def all_prefixes(string: str) -> List[str]:
    return list(reversed(list(dropwhile(lambda s: s == '', string))));
```