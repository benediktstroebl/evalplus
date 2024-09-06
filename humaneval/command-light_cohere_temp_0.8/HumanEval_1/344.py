```python
from typing import List
def separate_paren_groups(s: str) -> List[str]:
    return [part.group for part in s.group if ')' in part and ')' in part.group = ')'
group. 
    # balance and correct closing of the parentheses
    # ignore spaces
    return [] if ' ' in part else part
```