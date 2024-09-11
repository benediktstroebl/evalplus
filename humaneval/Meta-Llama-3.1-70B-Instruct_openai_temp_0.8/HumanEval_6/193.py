```python
from typing import List

def parse_nested_parens(paren_string: str) -> List[int]:
    """
    This function takes a string of multiple groups of nested parentheses separated by spaces.
    For each group, it returns the deepest level of nesting of parentheses.

    Args:
        paren_string (str): A string of multiple groups of nested parentheses separated by spaces.

    Returns:
        List[int]: A list of integers representing the deepest level of nesting for each group.
    """

    # Split the input string into groups of parentheses
    groups = paren_string.split()

    # Initialize an empty list to store the results
    results = []

    # Iterate over each group
    for group in groups:
        # Initialize a counter to keep track of the current nesting level
        current_level = 0

        # Initialize a variable to keep track of the maximum nesting level
        max_level = 0

        # Iterate over each character in the group
        for char in group:
            # If the character is an opening parenthesis, increment the current nesting level
            if char == '(':
                current_level += 1

                # Update the maximum nesting level if necessary
                max_level = max(max_level, current_level)
            # If the character is a closing parenthesis, decrement the current nesting level
            elif char == ')':
                current_level -= 1

        # Append the maximum nesting level for the current group to the results list
        results.append(max_level)

    # Return the list of results
    return results


# Test the function
print(parse_nested_parens('(()()) ((())) () ((())()())'))  # [2, 3, 1, 3]
```

In this script, we first split the input string into groups of parentheses. Then, for each group, we iterate over each character, keeping track of the current nesting level and the maximum nesting level. Finally, we append the maximum nesting level for each group to a results list and return the list. The time complexity of this script is O(n), where n is the total number of characters in the input string.