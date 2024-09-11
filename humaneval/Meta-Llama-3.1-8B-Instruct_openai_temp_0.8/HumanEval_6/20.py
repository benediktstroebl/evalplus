```python
from typing import List

def parse_nested_parens(paren_string: str) -> List[int]:
    """
    This function takes a string of nested parentheses separated by spaces as input.
    It returns a list of the maximum depth of nesting for each group of parentheses.

    :param paren_string: A string of nested parentheses separated by spaces
    :return: A list of the maximum depth of nesting for each group of parentheses
    """

    # Split the input string into groups of parentheses
    groups = paren_string.split()

    # Initialize an empty list to store the maximum depth of nesting for each group
    max_depths = []

    # Iterate over each group of parentheses
    for group in groups:
        # Initialize a counter to keep track of the current depth of nesting
        depth = 0
        # Initialize a flag to indicate whether we are currently inside a group of parentheses
        in_group = False
        # Initialize a flag to indicate whether we have seen a closing parenthesis that doesn't match with an opening parenthesis
        mismatch = False

        # Iterate over each character in the group
        for char in group:
            # If we encounter an opening parenthesis, increment the depth and indicate that we are inside a group
            if char == '(':
                depth += 1
                in_group = True
            # If we encounter a closing parenthesis and we are inside a group, decrement the depth
            elif char == ')':
                if in_group:
                    depth -= 1
                    # If the depth becomes negative, it means we have seen a closing parenthesis that doesn't match with an opening parenthesis
                    if depth < 0:
                        mismatch = True
                        break
                # If we are not inside a group, it's a mismatch
                else:
                    mismatch = True
                    break
            # If we encounter any other character, it's a mismatch
            elif not in_group and char!='':
                mismatch = True
                break

        # If we have seen a mismatch, append 0 to the list of maximum depths
        if mismatch:
            max_depths.append(0)
        # If the depth is 0, it means the group is not nested, so append 0 to the list of maximum depths
        elif depth == 0:
            max_depths.append(0)
        # Otherwise, append the maximum depth to the list of maximum depths
        else:
            max_depths.append(depth)

    # Return the list of maximum depths
    return max_depths

# Test the function
print(parse_nested_parens('(()()) ((())) () ((())()())'))
```

This script defines a function `parse_nested_parens` that takes a string of nested parentheses as input and returns a list of the maximum depth of nesting for each group of parentheses. The function iterates over each group of parentheses, keeping track of the current depth of nesting and checking for mismatches. If a mismatch is found, the function appends 0 to the list of maximum depths. Otherwise, the function appends the maximum depth to the list of maximum depths. The script also includes a test case to demonstrate the function's usage.