```python
from typing import List
def separate_paren_groups(s: str) -> List[str]:
    """
    Function to separate and return list of non-empty strings from a given string containing parentheses
    >>> separate_paren_groups('( )(( ))(( )()()'))
    ['()', '(())', '(()())']
    """
    return [e for e in s.replace(e) if e != '']
``` 
The function takes a string `s` as input and returns a list of non-empty strings separated by parentheses. It uses a certain formula to split the string on the spaces and then uses the `List.remove()` function to filter out any empty string from the resulting list.