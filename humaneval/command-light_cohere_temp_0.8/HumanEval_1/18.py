```python
from typing import List
def separate_paren_groups(s: str) -> List[str]:
    """Separate groups of parentheses into individual strings and return them as a list."""
    return [i for i in s.findall('([{}')] and [j for j in i.findall(')')]
```
This function uses the `findall()` method to iterate through each group of parentheses in the string `s`. It splits the string into individual groups of opening and closing parentheses and returns them as a list.