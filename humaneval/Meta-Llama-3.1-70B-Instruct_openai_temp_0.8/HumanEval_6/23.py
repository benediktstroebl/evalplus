```python
from typing import List

def parse_nested_parens(paren_string: str) -> List[int]:
    """
    This function takes a string of multiple groups of nested parentheses separated by spaces.
    It returns a list of integers representing the deepest level of nesting for each group.

    :param paren_string: A string of nested parentheses separated by spaces.
    :return: A list of integers representing the deepest level of nesting.
    """

    # Split the input string into groups of parentheses
    groups = paren_string.split()

    # Initialize an empty list to store the results
    results = []

    # Iterate over each group of parentheses
    for group in groups:
        # Initialize a counter for the current depth and the maximum depth
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

        # Append the maximum depth for the current group to the results
        results.append(max_depth)

    # Return the list of results
    return results


# Test the function
print(parse_nested_parens('(()()) ((())) () ((())()())'))  # [2, 3, 1, 3]
```