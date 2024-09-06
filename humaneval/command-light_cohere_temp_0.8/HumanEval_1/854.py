Here is a self-contained Python script that solves the problem of separating out the groups of parentheses in a given string:
```python
from typing import List
def separate_paren_groups(parentheses: str) -> List[str]:
    return [part.around() for part in parentheses.un()
```
```
This code defines a function called `separate_paren_groups` that takes a string of parentheses `parentheses` as input and returns a list of the cleaned up parentheses. The function uses a list comprehension to loop through the string and use the `unparse` method from the `string` module to remove the parentheses and backticks, and returns the resulting string.