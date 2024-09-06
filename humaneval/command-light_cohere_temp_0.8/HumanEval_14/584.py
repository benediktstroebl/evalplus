```python
from typing import List
def all_prefixes(string: str) -> List[str]:
    return [''.join(char) for char in string if char != ' ']
def test():
    assert all_prefixes('abc') == ['a', 'ab', 'abc']
```
This script defines a function all_prefixes that returns a list of all prefixes of a given string. It uses list comprehension with a character filter that only includes non-space characters. The test function asserts that the function produces the correct output for the string 'abc'.