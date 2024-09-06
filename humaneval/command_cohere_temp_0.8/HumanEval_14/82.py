```python
from typing import List
from itertools import accumulate


def all_prefixes(string: str) -> List[str]:
    """ Return list of all prefixes from shortest to longest of the input string """
    return list(accumulate(string[1:::-1]))
```
The function `all_prefixes()` uses the `accumulate()` function to create a list of all prefixes of the input string. The strings are iterated in reverse order and every two consecutive strings are concatenated to create a new prefix. The prefixes are then reversed to ensure they are in ascending order of their length, from the shortest to the longest.  It is important to note that the input string parameter should be of type `str` for the code to work properly. You can verify the function using the following tests:
```python
def test_all_prefixes():
    assert all_prefixes('abc') == ['a', 'ab', 'abc']
    assert all_prefixes('hello') == ['', 'h', 'he', 'hello']
    assert all_prefixes('world') == ['', 'w', 'wo', 'world']
    assert all_prefixes('longerandmorecomplex') == ['', 'l', 'lo', 'long', 'longer', 'longerma', 'longerand', 'longerandm', 'longerandmore', 'longerandmorec', 'longerandmorecom', 'longerandmorecomplex']
``` 
Ensure that the list of prefixes is in the expected order for each test case.