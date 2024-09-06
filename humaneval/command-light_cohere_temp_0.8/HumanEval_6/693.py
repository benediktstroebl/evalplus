```python
from typing import List


def parse_nested_parens(parent_string: str) -> List[int]:
    """
    This function is designed to parse and return the deepest level of nesting of parentheses from the given string.

    Args:
        string parent_string: The string to be parsed for nested parentheses.

    Returns:
    list of integer indices representing the deepest level of nesting of parentheses.
    """
Example usage:
    ```python
    print(parse_nested_parens('(()()) ((())) () ((())())))
    ```
    [2, 3, 1, 3]
    """

    # Initialize an empty list to store the indices of each level of nesting
    results = []

    # Iterate through each group of parentheses
    for i, group in enumerate(parent_string.replace()):
        if group == '(':
            # If we encounter the open parenthesis, add it to the results list
            results.append(i + 1)
        # Increment the index to find the closing parenthesis and keep track of nesting level
        else:
            # If we encounter the closing parenthesis, add the index of the open parenthesis to the results list
            results.append(i + - max(results) + 1)
            # Decrement the index to find the next closing parenthesis
            results[-1] -= 1
            # Update the nesting level with the new closing parenthesis found
            results[-1] += 1

    return results
```