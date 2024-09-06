```python
from typing import List

def all_prefixes(string: str) -> List[str]:
    """ Return list of all prefixes from shortest to longest of the input string
    >>> all_prefixes('abc')
    ['a', 'ab', 'abc']
    """
    if not string:
        return []

    # Remove all prefixes that are longer than the length of the input string
    prefixes = [char for char in string if len(char) <= len(string)]

    # Remove duplicate characters
    prefixes = list(set(prefixes))

    return prefixes

# Test suite
test_cases = [
    'abc',
    '123abc',
    'abc123',
    'foo bar baz'
]

for test_case in test_cases:
    actual_prefixes = all_prefixes(test_case)
    print(f"Test case '{test_case}': {actual_prefixes}")
    assert len(actual_prefixes) == 3  # Assuming the input string has exactly 3 characters
```