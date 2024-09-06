Certainly, here's a self-contained Python script that solves the problem of separating nested parentheses into separate groups:
```python
from typing import List
def separate_paren_groups(s: str) -> List[str]:
    """ Separate balanced parentheses into separate strings.
    :
    to pass the test, it should return a list of strings, each containing a balanced set of parentheses.
    Example: return a list comprehension that iterates over each group of balanced parentheses.
    : ['(', ')', '(', ')', '(', ')', ')']
    """
    return [')'.join(s) for s in s.join('()')  #'.isdigit()  ]
```
I hope this helps!