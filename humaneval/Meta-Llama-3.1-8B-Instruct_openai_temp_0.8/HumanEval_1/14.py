```python
from typing import List

def separate_paren_groups(paren_string: str) -> List[str]:
    """
    Input to this function is a string containing multiple groups of nested parentheses.
    Your goal is to separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.

    Args:
    paren_string (str): Input string containing multiple groups of nested parentheses.

    Returns:
    List[str]: A list of strings, each containing a separate group of nested parentheses.
    """

    # Remove spaces from the input string
    paren_string = paren_string.replace(" ", "")

    # Initialize stack and result list
    stack = []
    result = []

    # Iterate over each character in the string
    for char in paren_string:
        # If the character is an open parenthesis, push it onto the stack
        if char == "(":
            stack.append(char)
        # If the character is a close parenthesis, pop the corresponding open parenthesis from the stack
        elif char == ")":
            temp = ""
            while stack and stack[-1] == "(":
                temp = stack.pop() + temp
            # If the stack is empty after popping, it means there was a mismatched open parenthesis, so skip this group
            if not stack:
                continue
            # If temp is not empty, it means there was a nested group, so add it to the result list as a separate group
            if temp:
                result.append("({" + temp + "})")
            else:
                result.append("(" + ")"[1:len(stack)+1])
            # Reset the stack
            stack = []

    # Add any remaining groups to the result list
    for char in stack:
        temp = ""
        while stack and stack[-1] == "(":
            temp = stack.pop() + temp
        if temp:
            result.append("(" + temp + ")")

    return result


# Test the function
print(separate_paren_groups('( ) (( )) (( )( ))'))
```

This script defines a function `separate_paren_groups` that separates groups of nested parentheses in a given string. It uses a stack to keep track of the nested groups. When it encounters a close parenthesis, it pops the corresponding open parenthesis from the stack and adds it to the result list as a separate group. If there are any remaining groups after processing the entire string, it adds them to the result list. The function finally returns the list of separate groups.