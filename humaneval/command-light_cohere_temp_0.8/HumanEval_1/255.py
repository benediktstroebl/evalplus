```python
from typing import List

def separate_paren_groups(s: str) -> List[str]:
    """
    This function takes a string containing multiple groups of parentheses as input and returns a list of separated parenthesis groups.
    A single group is the nested and balanced parentheses are returned as individual strings, without any spaces.
    """

    list comprehension and regular expressions to separate the groups of parentheses.

Tests:
>>> test_string = "()"
>>> separate_paren_groups(test_string)
['()']
>>> test_string = "("
>>> separate_paren_groups(test_string)
['('')
>>> test_string = "((()))"
>>> separate_paren_groups(test_string)
['( )()]
>>> test_string = "(())(())"
>>> separate_paren_groups(test_string)
['())', '()()']
```