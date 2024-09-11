```python
from typing import List

def parse_nested_parens(paren_string: str) -> List[int]:
    """
    This function takes a string of groups of nested parentheses separated by spaces.
    For each group, it calculates the deepest level of nesting of parentheses.

    Args:
        paren_string (str): A string of groups of nested parentheses separated by spaces.

    Returns:
        List[int]: A list of deepest levels of nesting for each group.
    """
    result = []
    for group in paren_string.split():
        nesting_level = 0
        max_level = 0
        for i, char in enumerate(group):
            if char == '(':
                nesting_level += 1
                max_level = max(max_level, nesting_level)
            elif char == ')':
                nesting_level -= 1
            if nesting_level < 0:
                raise ValueError("Unbalanced parentheses in the input string.")
        result.append(max_level)
    return result

# Example usage:
print(parse_nested_parens('(()()) ((())) () ((())()())'))
```

This script works by iterating over each group of parentheses in the input string. For each group, it keeps track of the current nesting level (i.e., the number of unbalanced opening parentheses) and the maximum nesting level seen so far. It updates the maximum nesting level whenever it encounters a new unbalanced opening parenthesis or a balanced closing parenthesis. If it encounters a closing parenthesis when the nesting level is already zero, it means the parentheses in the group are unbalanced, and it raises a ValueError. Finally, it appends the maximum nesting level for each group to the result list.