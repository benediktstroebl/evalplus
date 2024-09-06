```python
from typing import List
def separate_paren_groups(parenthesis_string: str) -> List[str]:
    """
    Input to this function is a string containing multiple groups of nested parentheses. Return a list of the balanced parentheses.
    Separation rules:
    1. Balance all open parentheses.
    2. Balance all closed parentheses and balanced.
    3. Maintains a area balance from any spaces, as long as no other character is present.
    """
    return [parent_string.replace(lambda x: x.split('() )
    if x.count('(') == 1 else:
    ['(' + x + '')])
    else:
    return ['('] + x + '') + ['('] + '(']
    """
tests = [
    '()',  # Balanced
    '(())',  # Balanced
    '(()())',  # Balanced
    '((()))',  # Balanced
    '()()()',  # Unbalanced
    '()()((()))',  # Unbalanced
    '((()))())',  # Unbalanced
    '()(( ))'
]

for test_str in tests:
    assert separate_paren_groups(test_str) == test_str.  # Test if the invalid input string, it should return the original string.