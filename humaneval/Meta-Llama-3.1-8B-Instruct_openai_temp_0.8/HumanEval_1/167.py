```python
from typing import List
import itertools

def separate_paren_groups(paren_string: str) -> List[str]:
    """
    Input to this function is a string containing multiple groups of nested parentheses.
    Your goal is to separate those group into separate strings and return the list of those.
    
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.

    Args:
        paren_string (str): A string containing multiple groups of nested parentheses.

    Returns:
        List[str]: A list of strings, each representing a group of balanced parentheses.
    """
    
    # Remove spaces from the input string
    paren_string = paren_string.replace(" ", "")

    # Initialize an empty list to store the result
    result = []
    
    # Generate all possible splits of the string
    for r in range(1, len(paren_string)):
        # Split the string at each possible position
        for i in range(len(paren_string) - r):
            # Split the string into two parts
            left = paren_string[:i + r]
            right = paren_string[i + r:]
            
            # Check if both parts are balanced
            if is_balanced(left) and is_balanced(right):
                # If both parts are balanced, add them to the result
                result.append('(' + left + ')(' + right + ')')
    
    return result


def is_balanced(s: str) -> bool:
    """
    Check if a string of parentheses is balanced.

    Args:
        s (str): A string of parentheses.

    Returns:
        bool: True if the string is balanced, False otherwise.
    """
    stack = []
    
    # Iterate over each character in the string
    for char in s:
        # If the character is an open parenthesis, push it onto the stack
        if char == '(':
            stack.append(char)
        # If the character is a close parenthesis, check if the stack is empty
        elif char == ')':
            # If the stack is empty, the string is not balanced
            if not stack:
                return False
            # If the stack is not empty, pop the open parenthesis from the stack
            else:
                stack.pop()
    
    # After iterating over the entire string, check if the stack is empty
    # If the stack is empty, the string is balanced
    return not stack


# Example usage:
print(separate_paren_groups('( ) (( )) (( )( ))'))
```