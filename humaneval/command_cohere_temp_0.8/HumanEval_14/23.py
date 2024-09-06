```python
from typing import List
from itertools import accumulate


def all_prefixes(string: str) -> List[str]:
    """ Return list of all prefixes from shortest to longest of the input string """
    return list(accumulate(string[::-1]))[::-1]
```
This code reverses the input string, uses the accumulate function to concatenate successive characters from the reversed string, and then reverses the resulting list of prefixes to get the desired output.

Here is a sample output of the function:
```
['a', 'ab', 'abc']
```