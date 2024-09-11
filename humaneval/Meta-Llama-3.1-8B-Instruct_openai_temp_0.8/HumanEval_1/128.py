```python
from typing import List

def separate_paren_groups(paren_string: str) -> List[str]:
    """Input to this function is a string containing multiple groups of nested parentheses. 
    Your goal is to separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.

    Args:
    paren_string (str): A string containing multiple groups of nested parentheses

    Returns:
    List[str]: A list of separate groups of nested parentheses
    """
    # Remove all spaces from the input string
    paren_string = paren_string.replace(' ', '')

    # Initialize an empty stack and a list to store the substrings
    stack = []
    substrings = []

    # Initialize an empty substring
    substring = ''

    # Iterate over each character in the string
    for char in paren_string:
        # If the character is an open parenthesis, push it onto the stack and add it to the current substring
        if char == '(':
            stack.append(char)
            substring += char
        # If the character is a close parenthesis, pop the corresponding open parenthesis from the stack and add it to the current substring
        elif char == ')':
            stack.pop()
            substring += char
            # If the stack is empty after popping, it means we've found a complete substring, so add it to the list and reset the substring
            if not stack:
                substrings.append(substring)
                substring = ''
        # If the character is not a parenthesis, do nothing

    # Return the list of substrings
    return substrings

# Test the function
print(separate_paren_groups('( ) (( )) (( )( ))'))
```

This script uses a stack to keep track of the open parentheses and a list to store the substrings. It iterates over each character in the input string, pushing open parentheses onto the stack and popping corresponding close parentheses off the stack. When it encounters a close parenthesis that corresponds to an empty stack, it means it has found a complete substring, so it adds it to the list and resets the substring.