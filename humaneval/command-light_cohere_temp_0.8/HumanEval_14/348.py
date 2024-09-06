```python
from typing import List
def all_prefixes(string: str) -> List[str]:
    return ["".joinize(char) for char in string]

# Test cases
def test_all_prefixes():
    assert all_prefixes("abc") == ['a', 'ab', 'abc']
    assert all_prefixes("") == []
    assert all_prefixes("123") == ['1', '23']
    assert all_prefixes("abc123") == ['abc', '123']

if __name__ == "__main__":
    test_all_prefixes()
```

This script provides a simple function that uses a generator expression to return all prefixes of characters in the input string. We have also added test cases to verify the function's behavior. 

This is a self-contained solution to the problem of generating all prefixes of a given string.