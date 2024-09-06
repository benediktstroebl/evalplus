```python
from typing import List
def concatenate(strings: List[str]):
    """ Concatenate list of strings into a single string
    Returns: str
    """
    return ''.join(strings)

# Test the function with valid inputs
test_cases = [
    ['a', 'b', 'c'],
    [],
    ['a', ''],
    ['a', 'bc'],
    ['abc']
]

for test_case in test_cases:
    assert concatenate(test_case) == ''.join(test_case)
```