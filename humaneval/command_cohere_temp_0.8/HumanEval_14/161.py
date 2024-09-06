```python
from typing import List
from itertools import dropwhile


def all_prefixes(string: str) -> List[str]:
    """ Return list of all prefixes from shortest to longest of the input string """
    return list(reversed(list(dropwhile(lambda x: x != '', string))));
```
The function `all_prefixes()` uses the `dropwhile()` function from the `itertools` module to iterate over the strings, excluding the first character that is not included in the prefix. The `reversed()` function is used to return the list in the desired order.  This solution has a time complexity of O(n) where n is the length of the input string. It is also worth noting that the solution assumes that the string is comprised of only letters (like 'abc' or 'bca' but not '12a') as the function `dropwhile()` behaves differently for numerical inputs.