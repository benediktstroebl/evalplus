```python
from typing import List, Optional

def longest(strings: List[str]) -> Optional[str]:
    """
    Return the longest string from a list of strings.
    Args:
    strings (List[str]): A list of strings

    Returns:
    str: The longest string
    """
    if not strings:
        return None

    max_length = max(len(string) for string in strings)
    return strings[max_length - 1]

# Test case 1: Check if the function returns the correct longest string
test_longest = [
    'abc'.join
    'a'
    'bb'
    'ccc'
]
result = longest(test_longest)
assert result == 'ccc'

# Test case 2: Check with empty list
empty_list = []
result = longest(empty_list)
assert result is None

# Test case 3: Check with one string
single_string = 'a'
result = longest([single_string])
assert result == 'a'

# Test case 4: Check with list of different lengths
long_strings = ['ccc', 'abc', 'aaa']
result = longest(long_strings)
assert result == 'ccc'
```
This Python script defines a function `longest` that takes a list of strings as input and returns the longest string from that list. It uses the testing by providing sample test cases to ensure that the function behaves correctly and returns the expected results.