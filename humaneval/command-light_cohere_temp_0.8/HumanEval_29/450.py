```python
from typing import List


def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [s for s in strings if s.startswith(prefix)]


# Run tests
test_strings = [
    'abc', 'cde', 'a b cd', 'array'
    # Add more strings for more test cases
]
test_cases = [(s, prefix) for s, p in test_strings if filter_by_prefix(strings, p)]

def test_filter_by_prefix():
    assert test_cases == [(s.startswith('a'), 'a'*2] for s in strings]

test_filter_by_prefix()
``` 
This code defines a function `filter_by_prefix` that filters an input list of strings, returning only those that start with a specified prefix. The test suite is then added to ensure the function's correctness.  The testing uses the code to check if the function is returning the expected results for a given input.