```python
from typing import List

def all_prefixes(string: str) -> List[str]:
    return [''.join(char) for char in string if char != ''] + ['']

# Tests
def test_prefixes():
    assert all_prefixes('abc') == ['a', 'ab', 'abc']

test_prefixes()
```
This script defines a function `all_prefixes` that returns a list of all prefixes of a given string, it then provides a test function `test_prefixes` to run the function and check if the output matches the expected output.  This In a essential approach is using list comprehension to generate the list of prefixes and an empty string `[]` to ensure there's always a separator between the prefixes.