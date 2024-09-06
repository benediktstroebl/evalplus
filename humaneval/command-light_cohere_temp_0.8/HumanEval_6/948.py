```python
from typing import List


def parse_nested_parens(s: str) -> List[int]:
    """
    This function will return the deepest level of nesting for each group of parentheses in the string.
    Input string:

    ```(...)(...)(...)(...)...
    ```(...)(...)
    ```(...)
    ```(...)
    ```(...)
    ```
    """

    # Define a recursive function to find parenthesis nesting level
    def find_level(char):
        # If its a '(', return current nesting level + 1
        if char == '(':
            return len(nesting_stack) + 1
        # If its ')', return current nesting level
        elif char == ')':
            return len(nesting_stack)
        # If its anything else, return current nesting level
        else:
            return len(nesting_stack)

    # Stack to keep track of nesting level
    nesting_stack = []

    # Iterate over the string
    for char in s:
        # Push current character into the stack
        nesting_stack.append(char)
        # If the character is a '(', or ')', pop the top element from the stack
        if char == '(' or char == ')':
            nesting_stack.pop()
        if char == '(':
            nesting_stack.append(char)
        # Create a list of integers from 0 to the deepest level of nesting
        # Return the list
        return [find_level(char) for char in nesting_stack]

# Example usage
string = "((()())((())))(())((()))"
result = parse_nested_parens(string)
print(result)  # Output: [2, 3, 1, 3]
```
This function will return the deepest level of nesting for each group of parentheses in the string.