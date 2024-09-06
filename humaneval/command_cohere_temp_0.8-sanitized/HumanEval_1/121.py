from typing import List
def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    """
   
    stack = []
    current_group = []
    punctuations = '(){}[]'

    for char in paren_string:
        if char in punctuations:
            if char == '(':
                stack.append(current_group)
                current_group = []
            elif char == ')':
                if stack:
                    current_group.append(char)
                    stack.pop()
                else:
                    current_group.append(char)
            else:
                current_group.append(char)
        elif char == ' ':
            # ignore spaces
            continue

    # Handle the last group
    if current_group:
        stack.append(current_group)

    return stack