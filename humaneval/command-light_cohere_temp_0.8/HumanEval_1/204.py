```python
from typing import List
def separate_paren_groups(parenthesis_string: str) -> List[str]:
    """
    Separate groups of balanced parentheses into separate strings.
    Returns a balance and proper grouping of each set of parentheses.
    """
    test case:
    >>> test_case = '()( )(( ))((()) )'
    >>> separate_paren_groups(test_case)
    ['(', ')', '(', '()', '()', '())']
    """
    return [c for c in parenthesis_string if c == '('] + [c for c in parenthesis_string if c == ')']
```
This function takes a string containing multiple groups of parentheses as an argument and returns a list of separate strings, each containing a balanced group of parentheses. It uses list comprehension to iterate over each character in the string, and if the character is an open parenthesis '(', it adds it to the list of strings. The function also uses list comprehension to iterate over each character in the string, and if the character is a close parenthesis ')', it also adds it to the list of strings.