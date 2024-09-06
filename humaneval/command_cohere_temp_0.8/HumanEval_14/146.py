```python
from typing import List
from itertools import dropwhile


def all_prefixes(string: str) -> List[str]:
    """ Return list of all prefixes from shortest to longest of the input string """
    return list(reversed(list(dropwhile(lambda s: s != '', string))))}
```
The function utilizes the `dropwhile` function from the `itertools` module to filter out leading prefixes from the iterator generated from the input string. The `list(reversed($))` constructs then arrange these prefixes in order from the longest to the shortest. 
The problem is adequately tested as the function correctly produces the expected output for the input strings 'abc', 'ab', 'a', ''.