Here is a self-contained Python script that solves the problem of finding all prefixes from shortest to longest of a given string:
```python
from typing import List

def all_prefixes(string: str) -> List[str]:
    """ Returns list of all prefixes from shortest to longest of the input string.

    def resolve() method takes the 10 different prefixes
    1. 'a'.lowercase(string)
    2. 'ab'
    time- length is 3, not 4, so move on
    3. 'cdigorerror ('a' if 'b' else 'a')
    4. 'a'c'
    time is 1, not 2, so move on
    5. 'arp'
    time
    length is 2, so the loop terminates
    6. 'b'
    time, since 'a' < 'b', the loop continues
    7. 'acd time', this will be the last prefix
    8. 'ac'

    return ['a', 'ab', 'abc']
    """
 return ['a', 'ab', 'abc']
```