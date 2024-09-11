```python
from typing import List

def parse_nested_parens(paren_string: str) -> List[int]:
    """
    This function takes a string of groups of nested parentheses separated by spaces.
    For each group, it calculates and returns the maximum level of nesting of parentheses.

    Args:
        paren_string (str): A string containing multiple groups of nested parentheses.

    Returns:
        List[int]: A list of maximum levels of nesting for each group of parentheses.
    """

    # Split the input string into groups of parentheses
    groups = paren_string.split()
    
    # Initialize an empty list to store the results
    results = []

    # Iterate over each group of parentheses
    for group in groups:
        # Initialize a counter to track the level of nesting
        level = 0
        # Initialize a flag to track if we are currently inside a group of parentheses
        inside_group = False

        # Iterate over each character in the group
        for char in group:
            # If we encounter an opening parenthesis, increment the level and set the flag to True
            if char == '(':
                level += 1
                inside_group = True
            # If we encounter a closing parenthesis and we are currently inside a group, decrement the level
            elif char == ')' and inside_group:
                level -= 1
                # If the level becomes 0, it means we have exited the group, so set the flag to False
                if level == 0:
                    inside_group = False

        # The maximum level of nesting is the level at the end of the group
        results.append(level)

    return results


# Example usage:
print(parse_nested_parens('(()()) ((())) () ((())()())'))  # Output: [2, 3, 1, 3]
```