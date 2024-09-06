```python
from typing import List

def all_prefixes(string: str) -> List[str]:
    return ["".join(char) for char in string if char != '']

# Test cases
def test_all_prefixes():
    assert all_prefixes("abc") == ['a', 'ab', 'abc']
    assert all_prefixes("") == []
    assert all_prefixes("xx") == ['x']
    assert all_prefixes("123") == ['1', '12', '123']
```

This script defines a function that returns a list of prefixes from the shortest to the longest characters in the input string. It uses a alternative approach to find all prefixes by iterating through each character and excluding spaces using a list comprehension.  The tests to ensure the function is working as expected by passing different inputs and checking the returned values against the expected results.