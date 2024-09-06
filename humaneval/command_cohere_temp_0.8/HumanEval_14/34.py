```python
from typing import List
from itertools import accumulate


def all_prefixes(string: str) -> List[str]:
    """ Return list of all prefixes from shortest to longest of the input string """
    return list(accumulate([string[::-1], [string[:i]+string[i+1:] for i in range(len(string) + 1)][::-1]))[0]
```
The function leverages Python's `accumulate` function to generate all prefixes of the input string, and then reverses the list to ensure that the prefixes are ordered from shortest to longest. This solution has a complexity of O(n), where n is the length of the input string. 
It returns the list of all prefixes from the input string organized in the order of their lengthes, starting from the shortest one.