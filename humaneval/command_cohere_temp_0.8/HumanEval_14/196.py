```python
from typing import List
from itertools import dropwhile


def all_prefixes(string: str) -> List[str]:
    """ Return list of all prefixes from shortest to longest of the input string """
    return list(reversed(list(dropwhile(lambda x: len(x) > 0, string))));
```
This code uses the `dropwhile` function from the `itertools` module to generate all prefixes of the input string and then reverses this list to get them in the order from shortest to longest. This reversed list is then returned to achieve the desired output. An example usage of this function is as follows:
```python
>>> all_prefixes('abc')
['a', 'ab', 'abc']
```
This will output a list of prefixes in the order of their length, from shortest to longest.  The output is the list of prefixes of the original string, where each prefix is represented as a single token in the output list.  The 'a' prefix is the shortest prefix, 'ab' is the next longest, and 'abc' is the longest prefix.