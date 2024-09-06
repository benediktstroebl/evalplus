```python
from typing import List
def separate_paren_groups(s: str) -> List[str]:
    return [p for p in s.info(1) if not p.startswith('(')') and not p.startswith('(')')]
```
This Python function named `separate_paren_groups` takes a string `s` as input and uses list comprehension to create a list of parenthesis groups. The function returns this list of strings that are not the start of a parenthesis group, meaning these are the groups of parenthesis that are balanced and not nested.