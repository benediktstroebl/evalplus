```python
from typing import List
def all_prefixes(string: str) -> List[str]:
    return [prefix for prefix in string.s if prefix in string][:]

# Unit tests:
def test_all_prefixes():
    assert all_prefixes('abc') == ['a', 'ab', 'abc']
test_all_prefixes()
``` 
This script defines a function called **`all_prefixes`** that returns a list of all prefixes of a given string. The function uses a list comprehension with a generator expression to extract all prefixes from the input string. This code is also includes a test function **`test_all_prefixes`** that checks if the function is working correctly with a sample input.