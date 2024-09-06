```python
from typing import List
from itertools import dropwhile


def all_prefixes(string: str) -> List[str]:
    """ Return list of all prefixes from shortest to longest of the input string """
    return list(reversed(list(dropwhile(lambda x: len(x) > 0, string))));
```
This code uses the `dropwhile` function from the `itertools` module to generate all prefixes of the input string and then filters out the empty prefix. The `reversed` function is used to reverse the order of the prefixes since the `dropwhile` function drops elements from the beginning and leaves the longest prefixes at the beginning of the iterator. Thus, the list of prefixes is reversed to get them in the correct order, from shortest to longest.  It is important to use the `typing` module when defining the function to make its signature clear and improve code readability and maintainability. 

The function returns a list of all prefixes in the correct order.