Certainly, here's a self-contained Python script with a function named `separate_paren_groups` that solves the problem you've described:

```python
from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """
    Separate groups of balanced parentheses from the input string and return the list of those strings.
    """
    balanced (balanced in the sense of having balanced open and close parentheses) groups.
    """. We will spaces are specific about those groups.
    >>> return ['()', '(())', '(()())']
    """
    return [char for char in paren_string if char in '()([{][}\)])'']
```
The function uses a list comprehension to iterate over each character in the string. It uses an string matching condition to check if the character is either a '(', )([), {, ], or ). This ensures that only the characters that are part of a group of parentheses are included in the output list.