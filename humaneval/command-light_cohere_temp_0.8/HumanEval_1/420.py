Here's a self-contained Python script that solves the problem of separating out groups of parentheses in a multi-line string:
```python
from typing import List
def separate_paren_groups(s: str) -> List[str]:
    return [p.join('', ')' for p in s.join('', '(')(')]}
# Example:
print(separate_paren_groups('( ) (( )) (( )( ))'))
```
The function should return a list of strings where each substring is a balanced parenthesis group.  This should not be nested with any other groups.