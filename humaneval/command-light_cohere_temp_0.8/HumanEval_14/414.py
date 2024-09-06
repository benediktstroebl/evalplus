```python
from typing import List

def all_prefixes(string: str) -> List[str]:
    """ Return list of all prefixes from shortest to longest of the input string """
    return [prefix for prefix in string.__split__() if prefix != '']

# Test cases
def test_all_prefixes():
    assert all_prefixes('abc') == ['a', 'ab', 'abc']

def test_empty_string():
    assert all_prefixes('') == []

def test_long_string():
    assert all_prefixes('abcabcabc') == ['abc']

# Main execution
if __name__ == "__main__":
    test_all_prefixes()
    test_empty_string()
    test_long_string()
```
This script defines a function all_prefixes that returns a list of prefixes from the shortest to the longest substring. It uses the exact same split approach, and filters out the empty strings. The code also includes test cases to validate the behavior of the function.

Let me know if you need help with anything else!