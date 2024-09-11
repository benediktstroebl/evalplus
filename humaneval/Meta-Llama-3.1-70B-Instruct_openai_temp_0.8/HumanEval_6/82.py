```python
from typing import List

def parse_nested_parens(paren_string: str) -> List[int]:
    """
    This function calculates the maximum level of nesting in each group of parentheses.

    Args:
    paren_string (str): A string containing multiple groups of parentheses separated by spaces.

    Returns:
    List[int]: A list of integers representing the maximum level of nesting in each group.
    """
    groups = paren_string.split()
    result = []

    for group in groups:
        max_level = 0
        current_level = 0

        for char in group:
            if char == '(':
                current_level += 1
                max_level = max(max_level, current_level)
            elif char == ')':
                current_level -= 1

        result.append(max_level)

    return result


# Example usage:
print(parse_nested_parens('(()()) ((())) () ((())()())'))  # Output: [2, 3, 1, 3]
```

In this script, the `parse_nested_parens` function splits the input string into groups of parentheses and calculates the maximum level of nesting for each group. It does this by iterating over each character in the group, incrementing the current level when it encounters an opening parenthesis and decrementing it when it encounters a closing parenthesis. The maximum level encountered during this process is stored and added to the result list.