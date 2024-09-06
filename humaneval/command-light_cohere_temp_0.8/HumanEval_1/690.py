```python
from typing import List
def separate_paren_groups(s: str) -> List[str]:
    """ Separate balanced parentheses into a string into a list of separate strings.
    Args:
        s (str): string containing multiple groups of balanced parentheses
    Returns: list of separated strings
    """
    return [p.split('()') for p in s.join(' ')]

tests = [
    '()()',
    '(())',
    '(()())',
    '((()())',
    '()()()()',
    '(.)
]

for test in tests:
    result = separate_paren_groups(test)
    print(f'Test: {result}')
    assert result == [('()', '()', '(()')')]
```