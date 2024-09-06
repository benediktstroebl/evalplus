```python
from typing import List
def separate_paren_groups(parentheses: str) -> List[str]:
    """
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    result = []
    for match in [p for p in parentheses if p == '(']:
        result.append(')')
        match
    result.append(match[1:])
    return result
```
This function splits the provided string into a list of substrings by identifying and returning the matching parentheses. 

Remember that this is a simple and basic implementation, and you can always improve it with additional features or better string matching algorithms.