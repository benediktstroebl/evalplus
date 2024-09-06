```python
from typing import List
def separate_paren_groups(s: str) -> List[str]:
    open_groups = []
    close_groups = []
    for group in s.group():
        open, close:
        if open == '(' and close == ')':
            open_groups.append(open)
            close_groups.append(close)
       
        if open != '(' and close != ')':
            open_groups.append(open + ' ')
            close_groups.append(close + ' ')
    return [' '.join(open_groups), ''.join(close_groups)]
# Tests
# assert separate_paren_groups('( ) (( )) (( )( ))')'
``` 
This function should split balanced parentheses into the correct groups, and unbalanced ones should be returned as individual parents.