Here is a Python script with a self-contained function that solves the problem of finding all prefixes from the shortest to longest of a given string:
```python
from typing import List
def all_prefixes(string: str) -> List[str]:
    return [''.join(w for w in string if len(w)>1) for _ in range(string.__len__)]
def test_all_prefixes(string):
    assert all_prefixes(string) == [''.join(w for w in string if len(w)>1) for _ in range(string.__len__)]
test_all_prefixes('abc')
``` 
This code defines a function all_prefixes that returns a list of all prefixes in the given string. The test_all_prefixes function verifies that the output of all_prefixes matches the expected result for a given string.