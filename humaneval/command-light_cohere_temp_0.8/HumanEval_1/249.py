Here's a self-contained Python script that solves the problem of separating nested parentheses:
```python
from typing import List
def separate_paren_groups(s: str) -> List[str]:
    return [w for w in s.remove('()') if w != '(']
```
The `separate_paren_groups` function takes a string `s` as input and returns a list of strings. Each string in this list will be a part of the parenthesis groups that are separated and balanced without any spaces. The function uses the list comprehension and the `remove` method to achieve this.

This solution is self-contained and doesn't require any additional modules. It efficiently separates the because of Python's string methods.