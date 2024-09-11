```python
from typing import List

def parse_nested_parens(paren_string: str) -> List[int]:
    """
    Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.

    :param paren_string: String containing multiple groups of nested parentheses separated by spaces
    :return: List of deepest levels of nesting for each group
    """
    def nested_level(s: str) -> int:
        """
        Calculate the deepest level of nesting for a given string of nested parentheses
        :param s: String of nested parentheses
        :return: Deepest level of nesting
        """
        level = 0
        max_level = 0
        for char in s:
            if char == '(':
                level += 1
                max_level = max(max_level, level)
            elif char == ')':
                level -= 1
                # We do not need to check if level < 0 because the check for max_level should have taken care of it
        return max_level

    # Split the input string into groups and calculate the deepest level of nesting for each group
    return [nested_level(group) for group in paren_string.split()]
```

Example use case:
```python
print(parse_nested_parens('(()()) ((())) () ((())()())'))
# Output: [2, 3, 1, 3]
```