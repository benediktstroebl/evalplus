```python
from typing import List
from itertools import dropwhile


def all_prefixes(string: str) -> List[str]:
    """ Return list of all prefixes from shortest to longest of the input string """
    return list(reversed(list(dropwhile(lambda x: len(x) > 0, string[:-1:] + [string]))))
```
The function uses list comprehension and the `dropwhile` function from the `itertools` module to iterate over the strings descending from longest to shortest and including the empty string. The resulting list is then reversed to ensure that the order is from shortest to longest. 
The function returns a list of strings where each string is a prefix of the input string, ordered from shortest to longest. This list of prefixes contains the empty string at the beginning, followed by the shortest prefix, and so on to the longest prefix, which is the input string itself.