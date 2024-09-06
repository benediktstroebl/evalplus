```python
from typing import List
def all_prefixes(string: str) -> List[str]:
    return [''.join(c) for c in string if c.isalpha()]

def test_all_prefixes() -> None:
    assert all_prefixes('abc') == ['a', 'ab', 'abc']
test_all_prefixes()
``` 
This Python code defines a function `all_prefixes` that returns a list of all prefixes of a given string. The `test_all_prefixes` function is used to verify the correctness of the `all_prefixes` function by asserting that the result of calling it with the string 'abc' is a list containing 'a', 'ab', and 'abc'.