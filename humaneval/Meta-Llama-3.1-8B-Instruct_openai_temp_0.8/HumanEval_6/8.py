Here's a Python solution that uses a stack data structure to solve the problem.

```python
from typing import List

def parse_nested_parens(paren_string: str) -> List[int]:
    """
    Parse a string of nested parentheses and return the deepest level of nesting for each group.

    Args:
    paren_string (str): A string of multiple groups of nested parentheses separated by spaces.

    Returns:
    List[int]: A list of the deepest level of nesting for each group.

    """
    # Split the input string into groups of parentheses
    groups = paren_string.split()

    # Initialize an empty stack to keep track of the nesting level
    stack = []

    # Initialize an empty list to store the results
    results = []

    # Iterate over each group of parentheses
    for group in groups:
        # Initialize the max nesting level to 0
        max_nesting = 0

        # Initialize the current nesting level to 0
        nesting = 0

        # Iterate over each character in the group
        for char in group:
            # If the character is an opening parenthesis, push it onto the stack
            if char == '(':
                stack.append(char)
                # Increment the nesting level
                nesting += 1
                # Update the max nesting level if necessary
                max_nesting = max(max_nesting, nesting)
            # If the character is a closing parenthesis, pop the corresponding opening parenthesis from the stack
            elif char == ')':
                if stack:
                    stack.pop()
                    # Decrement the nesting level
                    nesting -= 1

        # Append the max nesting level for the current group to the results list
        results.append(max_nesting)

    # Return the list of results
    return results

# Test the function
print(parse_nested_parens('(()()) ((())) () ((())()())'))
```

This script uses a stack to keep track of the nesting level of the parentheses. For each group of parentheses, it iterates over each character and updates the nesting level accordingly. The max nesting level for each group is stored in the `results` list and returned at the end.