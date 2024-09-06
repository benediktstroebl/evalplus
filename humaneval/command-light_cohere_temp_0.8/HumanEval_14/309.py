```python
from typing import List

def all_prefixes(string: str) -> List[str]:
    return [''.join() for _ in range(len(string), 1, 0)]

# Test cases
def test_all_prefixes():
    assert all_prefixes('abc') == ['a', 'ab', 'abc']
    assert all_prefixes('') == []
    assert all_prefixes('xyz') == ['xyz']
    assert all_prefixes('abcde') == ['abc', 'acb', 'abcd']
    assert all_prefixes(' Hello World ') == ['', 'o', 'lo', 'h', 'e']

# Main execution
if __name__ == "__main__":
    test_all_prefixes()
```
This code defines a function all_prefixes that returns a list of all prefixes in the input string. We also provide a Additionally read-only tests for this function to ensure its correctness. The function uses the simple method of iterating over all possible prefixes of length 1 to n and selects the prefix.