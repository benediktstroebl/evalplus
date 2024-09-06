```python
from typing import List


def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [string for string in strings if string.startswith(prefix)]


# Test cases
test_cases = [
    ['abc', 'a'],  # matches
    ['cd', 'cd', 'c'],  # doesn't match
    ['hhi', 'hello'], # matches
    ['d', 'dd', 'dp'],  # doesn't match
    ['good', 'great'], # matches
    ['array', 'standing'], # matches
    ['a', 'b'],        # matches
    ['message', 'hello']  # doesn't match
]

# Function Testing
def test():
    assert filter_by_prefix(test_cases, 'a') == ['abc', 'array']
    assert filter_by_prefix(test_cases, 'cd') == []
    assert filter_by_prefix(test_cases, 'g') == []
    assert filter_by_prefix(test_cases, 'hello') == ['hhi']
    assert filter_by_prefix(test_cases, 'standing') == ['array']
    assert filter_by_prefix(test_cases, 'dp') == []
```
This Python script provides a function called `filter_by_prefix` that takes a list of strings and a prefix as input and returns a new list of strings that start with that prefix. The test cases provided help demonstrate the the usage of the function, passing in different strings and validating the expected outputs.