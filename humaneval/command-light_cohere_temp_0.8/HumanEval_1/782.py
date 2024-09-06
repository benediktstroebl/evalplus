```python
from typing import List
def separate_paren_groups(parentheses: str) -> List[str]:
    """
    Separate groups of parentheses into separate strings.
    Return list of strings
   
    """
    brackets = {')', '(', ')', ')', '{', '}', '[', ']', '(', '[', ']')
    result = []
    for bracket_pair in parentheses. Loop: for bracket in brackets:
        if bracket_pair.count(bracket) == 1:
            result.append(bracket)
            bracket_pair.count(bracket) = 0
    return result
```