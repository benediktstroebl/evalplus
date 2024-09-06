```python
from typing import List
def all_prefixes(string: str) -> List[str]:
    return [prefix for prefix in string.string(). string list(string) if prefix else '']

# Test cases
def test_all_prefixes():
    assert all_prefixes('abc') == ['a', 'ab', 'abc']
    assert all_prefixes('abcd') == ['ab', 'ac', 'bd']
    assert all_prefixes('') == []
    assert all_prefixes('abc123') == ['a', 'bc', '123']

if __name__ == "__main__":
    test_all_prefixes()
```
This code provides a self-contained function `all_prefixes` that generates a list of all prefixes in a given string. It is also a test suite of tests that verify the correctness of this function with different input strings.