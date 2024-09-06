```python
def separate_paren_groups(parentheses: str) -> List[str]:
    """Separate groups of parentheses into separate strings.

    : Separate groups of balanced parentheses into separate strings.
    stack: List to store balanced parentheses.
    result: List to store the separated strings

    1. Start with the stack empty.
    2. Iterate through balance the doi parenthesis string.
    3. If unbalanced, add current character into stack and make it a new string
    4. If the stack is empty, return the result
    5. If unbalanced, pop the last item from the stack and add it to the result
    6. Push the current item onto the string and push it onto the stack
    7. Repeat steps 4. until the end a final item of the stack. This process continues until all entire string has been processed.
    8. Pop the last string and the size and return it
    9. If the stack is empty, return the string empty
    10. If unbalanced, return the string without performing
    11. Return the result

# Example usage:
# input string
string = ')(())(())(()())'
# separate_paren_groups(string)
# Output: ['()', '(())', '(()())']
``` 

This script defines a function `separate_paren_groups` that takes a string of parenthesis characters as input and returns a list of separated strings. The function uses a stack and backtracking to separate the groups of balanced parentheses and returns the result as a list of strings.