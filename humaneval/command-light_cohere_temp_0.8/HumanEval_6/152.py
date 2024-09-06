```python
from typing import List


def parse_nested_parens(parent_string: str) -> List[int]:
    """
    This function takes a string of nested parentheses as input and returns a list of the deepest levels of nesting.
    """
    Input string is formatted as: <Group><Group><Group><arg></Group>
    """
    return [i for i, ch in enumerate(parent_string.replace()) if ch.startswith('('(') and parent_string.contains(ch[1]) and not parent_string.contains(ch[0)]]
```

This code defines a function **`'parse_nested_parens'`** that takes a string of nested parentheses as input and returns a list of the deepest levels of nesting for each group. The function uses a list comprehension to iterate through each character in the string. It checks if the grouping begins with open parentheses and if the current character is the right parenthesis closing the group. If the character matches the open parentheses, the group's depth is added to the output list. If it's right parenthesis and the current character is not an open parenthesis, the group's depth is not added. The function returns the list of the deepest levels of nesting found in the input string.