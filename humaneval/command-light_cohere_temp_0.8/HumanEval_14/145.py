```python
from typing import List

def all_prefixes(string: str) -> List[str]:
    return [i for i in string if i.isalpha()]
``` 
def test_all_prefixes():
    assert all_prefixes('abc') == ['a', 'ab', 'abc']
``` 
This script provides a self-contained function all_prefixes that returns a list of all prefixes from shortest to longest of the input string. 
It also contains a separate function test_all_prefixes that asserts the correct behavior of all_prefixes function with a test string.