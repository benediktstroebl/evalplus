```python
from typing import List

def parse_nested_parens(paren_string: str) -> List[int]:
    """
    This function takes a string of multiple groups of nested parentheses separated by spaces.
    It returns a list of integers representing the deepest level of nesting for each group.

    Args:
        paren_string (str): A string of multiple groups of nested parentheses separated by spaces.

    Returns:
        List[int]: A list of integers representing the deepest level of nesting for each group.
    """
    groups = paren_string.split()
    result = []

    for group in groups:
        max_depth = 0
        current_depth = 0

        for char in group:
            if char == '(':
                current_depth += 1
                max_depth = max(max_depth, current_depth)
            elif char == ')':
                current_depth -= 1

        result.append(max_depth)

    return result

# Example usage:
print(parse_nested_parens('(()()) ((())) () ((())()())'))  # Output: [2, 3, 1, 3]
```

This script defines a function `parse_nested_parens` that takes a string of multiple groups of nested parentheses separated by spaces. It splits the string into individual groups, initializes an empty list `result` to store the maximum depth for each group, and iterates over each group.

For each group, it initializes `max_depth` to 0 and `current_depth` to 0. It then iterates over each character in the group. If the character is an opening parenthesis `(`, it increments `current_depth` and updates `max_depth` if necessary. If the character is a closing parenthesis `)`, it decrements `current_depth`.

After processing each group, it appends the `max_depth` for that group to the `result` list. Finally, it returns the `result` list.

The example usage demonstrates how to call the function with a sample input string and print the output.