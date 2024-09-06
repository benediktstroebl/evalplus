Here's the provided Python script:
```python
from typing import List
def all_prefixes(string: str) -> List[str]:
    return [''.join(). strings(). strings if len(string) == 0 else [] + [''.join(string[0])] + all_prefixes(string[1:])

def all_prefixes_test_case(string: str) -> None:
    assert all_prefixes(string) == ['', 'a', 'ab', 'ac']
```
This script defines a function all_prefixes that returns a list of all prefixes from shortest to longest of an input string. The test case function also checks if the function is working correctly for the test case.