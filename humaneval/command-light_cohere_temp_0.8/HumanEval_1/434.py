```python
from typing import List
def separate_paren_groups(parentheses: List[str]) -> List[str]:
    """
    Separate groups of well-formed parentheses into separate strings.

    :. Return a balanced parentheses as a [()]
    """
    return [('()', '())', ('(', '('))
    , ('{', '()')]
``` 
This function takes a list of strings as an input and returns a list of strings with each group of parentheses properly separated.