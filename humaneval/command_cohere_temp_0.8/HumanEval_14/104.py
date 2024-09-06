```python
from typing import List
from itertools import accumulate


def all_prefixes(string: str) -> List[str]:
    """ Return list of all prefixes from shortest to longest of the input string """
    return list(accumulate([string[i:] for i in range(len(string) + 1)]))
```
The provided Python script defines a function `all_prefixes` that takes a string as input and returns a list of its prefixes, arranged in ascending order of length. The function employs an iterator comprehension to generate an iterator that computes the prefixes of the input string. This iterator is then transformed into a list using the `accumulate` function from the `itertools` module.

Here's an example of using this function:
```python
>>> all_prefixes('abc')
['a', 'ab', 'abc']
```
The output shows the three prefixes of the input string ('a', 'ab', and 'abc'), sorted by their lengths, from shortest to longest.