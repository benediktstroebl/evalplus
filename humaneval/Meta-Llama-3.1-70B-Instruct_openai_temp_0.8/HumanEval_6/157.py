```python
from typing import List

def parse_nested_parens(paren_string: str) -> List[int]:
    """
    This function calculates the maximum depth of nested parentheses in each group.

    Args:
        paren_string (str): A string containing multiple groups of nested parentheses separated by spaces.

    Returns:
        List[int]: A list of integers representing the maximum depth of nesting for each group.

    """
    # Split the input string into groups
    groups = paren_string.split()

    # Initialize an empty list to store the results
    results = []

    # Iterate over each group
    for group in groups:
        # Initialize variables to keep track of the current and maximum depth
        current_depth = 0
        max_depth = 0

        # Iterate over each character in the group
        for char in group:
            # If the character is an opening parenthesis, increment the current depth
            if char == '(':
                current_depth += 1
                # Update the maximum depth if necessary
                max_depth = max(max_depth, current_depth)
            # If the character is a closing parenthesis, decrement the current depth
            elif char == ')':
                current_depth -= 1

        # Append the maximum depth for the current group to the results list
        results.append(max_depth)

    # Return the list of results
    return results


# Example usage
print(parse_nested_parens('(()()) ((())) () ((())()())'))  # Output: [2, 3, 1, 3]
```

In this script, the `parse_nested_parens` function takes a string of multiple groups of nested parentheses as input, calculates the maximum depth of nesting for each group, and returns a list of integers representing the maximum depth for each group. The function uses a simple iterative approach to calculate the depth, incrementing the current depth for each opening parenthesis and decrementing it for each closing parenthesis. The maximum depth is updated whenever the current depth exceeds the previous maximum.