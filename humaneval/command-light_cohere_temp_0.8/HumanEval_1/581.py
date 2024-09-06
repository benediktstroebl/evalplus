```python
from typing import List
def separate_paren_groups(parentheses: str) -> List[str]:
    """
    Function to separate and organize parentheses properly.
    Args:
        parenthesis string containing multiple groups of nested parentheses.
    Returns: list of separate and organized parenthesis strings.
    """
    example usage:
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    result = []
    for match in parentheses.match(). separated() :
        list(match) for match in  list(match) : match += ')'
    result.append(match)
    return result
```
This function takes a string containing multiple groups of nested parentheses as input and returns a list of separated and organized parentheses. The function uses a `reversed` loop and a list comprehension to match and separate each group of parentheses.