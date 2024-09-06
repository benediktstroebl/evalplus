```python
from typing import List

def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [s for s in strings if s.startswith(prefix)]

# Unit tests
strings = ["abc", "bcd", "cde", "array", "hello", "world"]
prefix = "a"

# Function test cases
assert filter_by_prefix(strings, prefix) == ['abc', "array"]
assert not filter_by_prefix(strings, "x") == []

``` 
This code defines a function called `filter_by_prefix` that takes a list of strings and a prefix as input and returns a new list that contains elements that start with the specified prefix. It utilizes the test list comprehension to filter out elements that match the given prefix.