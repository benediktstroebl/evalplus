```python
from typing import List

def all_prefixes(string: str) -> List[str]:
    return [''.join(*map(str.join, string)) for i in range(1, len(string))+1]

# Test suite
def test_prefixes():
    assert all_prefixes('abc') == ['a', 'ab', 'abc']
    assert all_prefixes('abcd') == ['ab', 'ac', 'bd']
    assert all_prefixes('abcde') == ['abc', 'abcd', 'def']
    assert all_prefixes('') == []

if __name__ == "__main__":
    test_prefixes()
```
This script defines a function that returns a list of all prefixes from shortest to longest of an input string.  The provides a test suite with a few tests. The function and test suite are separated to ensure the function's self-containment and test its correctness independently.