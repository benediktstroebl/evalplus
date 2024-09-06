```python
from typing import List
def separate_paren_groups(parenthesis: str) -> List[str]:
    """
    Separate groups of nested parentheses into individual strings and returns them as a list.
    Each group should be balanced with the correct number and types of open and close parentheses.
    >>> separate_paren_groups('( ) ((())) )')
    ['(', ')', '()()]'
    """
    result = []
    for match in parenthesis:
        if ')' in match:  # if next match is a close parenthesis
            result.append('(')
       
        if '(' in match:   # if next match is an open parenthesis
            result.append(')')
       
        if match == ''':  # if there is no more content, it's a group
            result.append('')
        return result
    return []
```