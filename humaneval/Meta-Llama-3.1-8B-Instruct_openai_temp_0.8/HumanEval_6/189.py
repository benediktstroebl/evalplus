```python
from typing import List

def parse_nested_parens(paren_string: str) -> List[int]:
    """
    Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.

    Args:
        paren_string (str): A string of groups of nested parentheses separated by spaces.

    Returns:
        List[int]: A list of the deepest level of nesting of parentheses for each group.
    """
    groups = paren_string.split()
    results = []

    for group in groups:
        max_depth = 0
        current_depth = 0
        for char in group:
            if char == '(':
                current_depth += 1
                max_depth = max(max_depth, current_depth)
            elif char == ')':
                current_depth -= 1
                if current_depth < 0:
                    current_depth = 0  # Ignore unnecessary closing parentheses
        results.append(max_depth)

    return results

# Example usage:
print(parse_nested_parens('(()()) ((())) () ((())()())'))
```

In this script, the function `parse_nested_parens` takes a string of groups of nested parentheses as input, splits the string into groups, and then for each group, it counts the maximum depth of nesting by keeping track of the number of open parentheses encountered so far. The maximum depth is updated whenever a deeper opening parenthesis is encountered. Finally, it appends the maximum depth of each group to the results list. The function returns the list of maximum depths for all groups.