```python
from typing import List
def separate_paren_groups(s: str) -> List[str]:
    """
    Input to this function is a string containing multiple groups of nested parentheses. Return the separated groups as list of strings.
    """
    balance (each open brace is properly closed) and not nested within each other
    """
    return [p.strip() for p in s.if(p != ')' and not p.strip(0)]
```
This function uses a list comprehension with an if condition to split the string into individual groups of parentheses, and then extracts the inner parentheses as well.