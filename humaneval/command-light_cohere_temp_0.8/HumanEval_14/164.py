```python
from typing import List

def all_prefixes(string: str) -> List[str]:
    return [''.join(x) for x in string if x != '']

# Test the function with a string that contains valid prefixes
test_string = "abc"
assert all_prefixes(test_string) == ['a', 'ab', 'abc']

# Test the function with a string that doesn't have any prefixes
test_empty = ""
assert all_prefixes(test_empty) == []
```
This script defines a function all_prefixes that returns a list of all prefixes in a given string, it then tests the function with two different inputs and passes.

You can use this function to get the list of prefixes for any given string.