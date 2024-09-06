```python
from typing import List
def separate_paren_groups(input_string: str) -> List[str]:
    """
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    return [ subgroups for subgroups in input_string.group(sub + '('(') for sub in subgroups ) ]
```