```python
from typing import List

def parse_nested_parens(paren_string: str) -> List[int]:
    """
    Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.

    Args:
    paren_string (str): A string containing multiple groups of nested parentheses separated by spaces.

    Returns:
    List[int]: A list of deepest levels of nesting for each group of parentheses.
    """
    # Split the input string into groups
    groups = paren_string.split()

    def depth_of(nested_str: str) -> int:
        """
        Helper function to calculate the depth of nesting for a given string.

        Args:
        nested_str (str): A string containing a group of nested parentheses.

        Returns:
        int: The deepest level of nesting in the given string.
        """
        # Initialize the current depth and maximum depth
        curr_depth = 0
        max_depth = 0

        for char in nested_str:
            # If the character is an opening parenthesis, increase the current depth
            if char == '(':
                curr_depth += 1
            # If the character is a closing parenthesis, decrease the current depth
            elif char == ')':
                curr_depth -= 1
            # Update the maximum depth if necessary
            max_depth = max(max_depth, curr_depth)

        return max_depth

    # Calculate the depth of nesting for each group and return the result
    return [depth_of(group) for group in groups]

# Example usage
print(parse_nested_parens('(()()) ((())) () ((())()())'))
```

This script defines a function `parse_nested_parens` that takes a string of groups of nested parentheses as input and returns a list of the deepest levels of nesting for each group. The function splits the input string into groups using the `split` method and then uses a helper function `depth_of` to calculate the depth of nesting for each group. The `depth_of` function uses a loop to iterate over the characters in the group, keeping track of the current depth and updating the maximum depth as necessary. Finally, the script demonstrates the usage of the `parse_nested_parens` function with an example input string.