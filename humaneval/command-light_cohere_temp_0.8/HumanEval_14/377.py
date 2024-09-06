```python
from typing import List
def all_prefixes(string: str) -> List[str]:
    return [''.join(x) for x in string.
    pass
```
def test_prefixes():
    assert all_prefixes('abc') == ['a', 'ab', 'abc']
```
This code provides a function all_prefixes that returns a list of all prefixes in a passed string. 
The test_prefixes function runs the function with 'abc' and asserts the result.