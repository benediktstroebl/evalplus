```python
from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """
    This function takes a string of groups of nested parentheses separated by spaces.
    For each group, it returns the maximum level of nesting of parentheses.

    Args:
        paren_string (str): A string of groups of nested parentheses separated by spaces.

    Returns:
        List[int]: A list of the maximum level of nesting of parentheses for each group.
    """
    # Split the input string into groups
    groups = paren_string.split()

    def max_depth(s: str) -> int:
        # Initialize the maximum depth and current depth to 1
        max_depth = 1
        curr_depth = 1
        # Iterate over the parentheses
        for i in range(1, len(s)):
            # If we encounter a closing parenthesis, decrease the current depth
            if s[i] == ')':
                curr_depth -= 1
            # If we encounter an opening parenthesis, increase the current depth
            elif s[i] == '(':
                curr_depth += 1
            # Update the maximum depth if the current depth is greater
            max_depth = max(max_depth, curr_depth)
        # Return the maximum depth
        return max_depth

    # Calculate the maximum depth for each group and return the results
    return [max_depth(group) for group in groups]


# Test the function
print(parse_nested_parens('(()()) ((())) () ((())()())'))
```

This script uses a helper function `max_depth` to calculate the maximum depth of nesting for each group of parentheses. It iterates over the parentheses, increasing the current depth when it encounters an opening parenthesis and decreasing it when it encounters a closing parenthesis. It keeps track of the maximum depth seen so far and returns it at the end. The main function `parse_nested_parens` splits the input string into groups, calculates the maximum depth for each group using the `max_depth` function, and returns the results.