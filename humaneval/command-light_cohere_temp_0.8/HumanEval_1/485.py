Certainly! Here's a self-contained Python function that splits a string of parentheses into individual groups:
```python
from typing import List

def separate_paren_groups(parentheses: str) -> List[str]:
    """
    Separates a string of parentheses into individual groups and returns them as a list.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    return [part.replace(0, len(parentheses) - 1) for part in parentheses.strip("").replace('()', ' ')
    }
```

This function utilizes the `replace()` method to replace the parenthesis with a space, which makes the inner groups easier to be identified. The `part` variable iterates through each character of the string, except the last character before the next set of parentheses.