```python
from typing import List
def all_prefixes(string: str) -> List[str]:
    return [''.join(c) for c in string if c.isalpha()]

def test_all_prefixes():
    assert all_prefixes('abc') == ['a', 'ab', 'abc']
test_all_prefixes()  # run the function and check the output against the assert statement
```  This script provides a function `all_prefixes` that returns a list of all prefixes in a string, and a function `test_all_prefixes` that tests if the `all_prefixes` function is working correctly.  The run this test_all_prefixes() to execute the function and verify the output.