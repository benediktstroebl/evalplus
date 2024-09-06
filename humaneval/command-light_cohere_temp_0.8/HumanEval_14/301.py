```python
from typing import List

def all_prefixes(string: str) -> List[str]:
    """ Return list of all prefixes from shortest to longest of the input string """
    return sorted(string, key=len, reverse=True)[:-len(string) - 1:]

# Test cases
def test_all_prefixes():
    assert all_prefixes('abc') == ['a', 'ab', 'abc']

def test_empty_string():
    assert all_prefixes('') == []

def test_long_string():
    assert all_prefixes('verylongstring') == []

# Main program
if __name__ == "__main__":
    test_all_prefixes()
    test_empty_string()
    test_long_string()
```
This script defines a function `all_prefixes` that returns a list of all prefixes from the shortest to the longest characters in the input string. It is also includes several test cases to validate the correctness of the function.