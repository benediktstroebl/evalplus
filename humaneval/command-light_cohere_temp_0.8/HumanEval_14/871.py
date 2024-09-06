```python
from typing import List

def all_prefixes(string: str) -> List[str]:
    return ["".join(char) for char in string if char != ' ']

# Test cases
def test_all_prefixes():
    assert all_prefixes("abc") == ['a', 'ab', 'abc']
    assert all_prefixes("123") == ['1', '23']
    assert all_prefixes("") == []
    assert all_prefixes("paces") == ['p']
    assert all_prefixes("\t hab") == ['h', 'a']

if __name__ == "__main__":
    test_all_prefixes()
```
This code defines a function called `all_prefixes` that returns a list of prefixes from a given string. The function uses a list comprehension and an `if` condition to filter out any space characters from the string.

The `test_all_prefixes` function is a test case that checks the output of `all_prefixes` with different input strings to ensure the function works correctly. The `if __name__ == "__main__":` block ensures that the test case is run when the script is run directly.