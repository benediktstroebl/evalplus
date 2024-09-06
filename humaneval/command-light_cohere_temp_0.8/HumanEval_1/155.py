```python
from typing import List
def separate_paren_groups(parentheses: List[str]) -> List[str]:
    return [p.split('() for p in parentheses]
parentheses = ['( )((()))', '()', '(()())', '()', '( )']
# Test the function with a single string of parentheses
assert separate_paren_groups(parentheses) == ['()', '(())', '(()())', '()', '( ')];
```
This code defines a function called `separate_paren_groups`, which takes a list of strings as input and returns a list of separate parentheses. The function splits each string into a list of open parentheses and closes them, effectively separating the different groups of parentheses.