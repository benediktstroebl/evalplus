```python
from typing import List
def separate_paren_groups(s: str) -> List[str]:
    """
    Split parentheses into individual groups and return as a list.
    >>> '()( )(( ))(( ))'
    ['()', '( )', '(() )']
    """
    return [pair for pair in s.group() if not pair '()' or pair ')]'
``` 
The function uses a list comprehension to iterate over each group of parentheses in the string. This is then ignore spaces and return a list of strings.