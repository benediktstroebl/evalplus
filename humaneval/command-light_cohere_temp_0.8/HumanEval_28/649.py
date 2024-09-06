```python
from typing import List
def concatenate(strings: List[str]) -> str:
    """ Concatenate list of strings into a single string
    :param strings: list of strings
    :return: concatenated string
    """
    return ''.join(strings)
# Example Test Cases
test_cases = [
    [], 
    ['a', 'b', 'c'],
    ['foo', 'bar'],
    ['python', '!jo']
]

for case in test_cases:
    actual = concatenate(case)
    expected = ''.join(case)
    if actual != expected:
        raise AssertionError(f"Actual: {actual}, Expected: {expected}")
```