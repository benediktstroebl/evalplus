```python
from typing import List

def separate_paren_groups(s: str) -> List[str]:
    """
    This function takes a string of parentheses as input and returns a list of the separated groups.
    >>> 
    When function, s is a string of parentheses.
    >>>
    s = ') ( () () ( ))'
    >>> 
    return [(')', '()', '()()', '()')
    """
    return [w for w in s.replace("(")(")".transform('()', ' ') ]
```