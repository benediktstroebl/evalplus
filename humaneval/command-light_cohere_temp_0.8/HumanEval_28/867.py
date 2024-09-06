```python
from typing import List
def concatenate(strings: List[str]) -> str:
    """ Concatenate list of strings into a single string
    Args:
    strings (List[str]): List of strings to concatenate

    Returns:
    str: Concatenated string
    """
    return ''.join(strings)

# Test case 1
test_cases = [()]
result = concatenate(test_cases)
assert result == '', 'Test case 1 failed.'

# Test case 2
test_cases = ['a', 'b', 'c']
result = concatenate(test_cases)
assert result == 'abc', 'Test case 2 failed.'

# Test case 3
test_cases = ['a', 'b', '']
result = concatenate(test_cases)
assert result == 'ab', 'Test case 3 failed.'

print('All tests passed.')
```