```python
from typing import List

def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [string for string in strings if string.startswith(prefix)]

# Test case using pytest
def test_filter_by_prefix():
    assert filter_by_prefix([ 'abc', 'bcd', 'cde', 'array'], 'a') == ['abc', 'array']

# Run the function and check the output
test_filter_by_prefix()
```
This code defines a function called **`filter_by_prefix`** which takes a list of strings and a prefix as input and returns a new list that contains elements from the original list that start with the given prefix. It utilizes theator list comprehension to filter the strings by their prefix. The test case is included to ensure the function's correctness.