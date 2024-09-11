```python
from typing import List

def parse_nested_parens(paren_string: str) -> List[int]:
    """
    This function takes a string of multiple groups of nested parentheses separated by spaces.
    It returns a list of integers representing the deepest level of nesting for each group.

    :param paren_string: A string of multiple groups of nested parentheses separated by spaces.
    :return: A list of integers representing the deepest level of nesting for each group.
    """

    # Split the input string into groups of parentheses
    groups = paren_string.split()

    # Initialize an empty list to store the results
    results = []

    # Iterate over each group of parentheses
    for group in groups:
        # Initialize a counter to keep track of the current nesting level
        nesting_level = 0

        # Initialize a variable to keep track of the maximum nesting level
        max_nesting_level = 0

        # Iterate over each character in the group
        for char in group:
            # If the character is an opening parenthesis, increment the nesting level
            if char == '(':
                nesting_level += 1

                # Update the maximum nesting level if necessary
                max_nesting_level = max(max_nesting_level, nesting_level)

            # If the character is a closing parenthesis, decrement the nesting level
            elif char == ')':
                nesting_level -= 1

        # Append the maximum nesting level for the current group to the results list
        results.append(max_nesting_level)

    # Return the list of results
    return results


# Test the function
print(parse_nested_parens('(()()) ((())) () ((())()())'))  # Output: [2, 3, 1, 3]
```