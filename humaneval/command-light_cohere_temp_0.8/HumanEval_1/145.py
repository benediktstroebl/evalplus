```python
from typing import List
def separate_paren_groups(s: str) -> List[str]:
    return [p.center(c) for p, c in zip(['(', ')', ')', ')', ')] if c.isinstance('(')]
```
This code defines a function called `separate_paren_groups` that takes a string of parentheses as input and returns a list of separated parenthesis. The function uses a list comprehension and a lambda function to achieve this.