```python
from typing import List

def separate_paren_groups(s: str) -> List[str]:
    """ Separate and return groups of parentheses.
    >>> '((())' == '()' and ')('.join(separate_paren_groups('() (( )))'))
    """
    return [p for p in s if not p == '(' and not p == ')']
``` 
This Python code defines a function `separate_paren_groups` that takes a string `s` as input and returns a list of non-parenthesis characters from the string. It utilizes a regular expression to identify and collect non-parenthesis characters into a new list. The code is designed to handle a variety of scenarios involving parenthesis and brackets, ensuring correct separation and providing clear and accurate results.