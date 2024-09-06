```python
from typing import List
from itertools import dropwhile


def all_prefixes(string: str) -> List[str]:
    """ Return list of all prefixes from shortest to longest of the input string """
    return list(reversed(list(dropwhile(lambda x: len(x) > 0, string))));
```
The function `all_prefixes()` uses the `dropwhile` function from the `itertools` module to iterate over the characters of `string` but excludes those that have a length greater than 0 (i.e., the longest prefix). 
The result is reversed to ensure the prefixes are listed in the order of shortest to longest. 
The function returns a list of all the prefixes of the string in the desired order.