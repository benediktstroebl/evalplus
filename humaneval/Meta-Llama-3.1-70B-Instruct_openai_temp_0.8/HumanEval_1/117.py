```python
from typing import List

def separate_paren_groups(paren_string: str) -> List[str]:
    """
    Input to this function is a string containing multiple groups of nested parentheses.
    Your goal is to separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.

    :param paren_string: A string containing multiple groups of nested parentheses.
    :return: A list of strings where each string is a separate group of parentheses.
    """

    # Remove spaces from the input string
    paren_string = paren_string.replace(" ", "")

    # Initialize an empty stack and an empty list to store the result
    stack = []
    result = []
    temp = ""

    # Iterate over each character in the string
    for char in paren_string:
        # If the character is an open parenthesis, push it to the stack
        if char == "(":
            stack.append(char)
            temp += char
        # If the character is a close parenthesis, pop the corresponding open parenthesis from the stack
        elif char == ")":
            stack.pop()
            temp += char
            # If the stack is empty after popping, it means we have a complete group of parentheses
            if not stack:
                result.append(temp)
                temp = ""

    return result

# Example usage:
print(separate_paren_groups('( ) (( )) (( )( ))'))  # Output: ['()', '(())', '(()())']
```

This script works by iterating over the input string and pushing each open parenthesis onto a stack. When a close parenthesis is encountered, the corresponding open parenthesis is popped from the stack. If the stack is empty after popping, it means we have a complete group of parentheses, which is then added to the result list. The `temp` variable is used to build each group of parentheses as a string.