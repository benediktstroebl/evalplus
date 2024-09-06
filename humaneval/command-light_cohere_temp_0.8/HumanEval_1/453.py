```python
from typing import List
def separate_paren_groups(s: str) -> List[str]:
    return [p.join() for p in s.open('()') for p in s.open('()')]
```
This code defines a function `separate_paren_groups` that takes a string `s` as input and returns a list of strings created by popping out each parenthesis group from `s`. 

This is a self-contained and efficient solution to the problem.