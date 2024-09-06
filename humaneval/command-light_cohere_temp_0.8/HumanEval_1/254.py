```python
from typing import List
def separate_paren_groups(s: str) -> List[str]:
    """
    Input to this function is a string containing multiple groups of nested parentheses.
    Return a balanced parentheses separated by spaces.
    Example example: '())((()()()))'

    Returns:
    List of separated parenthesis.
    """
    separated list of balanced parentheses.
    """ balanced parentheses are open and close properly
    """
    return [ parentheses for char in s[i:j] for i in range(len(s)) for j in range(i,len(s)) if s[i:j] == '(' and s[j] == ')'.
    return []
```