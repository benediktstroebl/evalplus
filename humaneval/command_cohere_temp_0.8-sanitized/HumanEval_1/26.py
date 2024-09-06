from typing import List
def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    """
    # Using a stack to store parentheses groups
    stack = []
    current_group = ""

    # Iterating through each character in the input string
    for char in paren_string:
        if char == '(':
            # If the character is an open parenthesis, add it to the current group
            current_group += char
        elif char == ')':
            # If the character is a closing parenthesis, add it to the current group if the current group is not empty
            if current_group:
                current_group += char
            else:
                # If the current group is empty, it means there are unbalanced parentheses, so we skip the closing parenthesis
                continue
        else:
            # If the character is not a parenthesis, it is necessarily a space, so we ignore it
            continue

        # If the current group is not empty, we add the current group to the stack
        if current_group:
            stack.append(current_group)
            current_group = ""

    # Finally, we add the last group to the stack if it is not empty
    if current_group:
        stack.append(current_group)

    # Returning the list of strings representing each group of parentheses
    return stack