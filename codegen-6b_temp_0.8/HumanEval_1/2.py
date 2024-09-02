from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    # Use a stack to track what's inside the current group
    # Add the first char if it's a list
    stack = []
    if paren_string:
        stack.append([paren_string[0]])
    paren_string = paren_string[1:]
    # While we haven't popped every PBR
    while paren_string:
        char = paren_string[0]
        # If we're going to add a PBR
        if char == ')':
            # Pop the PBR if there is a left-over
            if stack:
                self_closing_group = stack.pop()
                # If the last group is a string, add it to the stack
                if isinstance(self_closing_group[-1], str):
                    stack.append([self_closing_group[-1]])
                    self_closing_group.pop()
            # If the last group isn't a string, we have an open group
            if isinstance(stack[-1][-1], str):
                stack[-1].append(char)
            else:
                stack.append([char])
        # If we're adding a new char, add it to the stack
        elif char == '(':
            stack.append([char])
        # If it's a space, ignore it
        elif char == ' ':
            pass
        # If it's a left-over char, add it to the last group
        else:
            if isinstance(stack[-1][-1], str):
                stack[-1].append(char)
            else:
                stack[-1].append(char)
        # Get the next char
        paren_string = paren_string[1:]
    # Combine the strings together
    results = []
    for self_closing_group in stack:
        self_closing_group = "".join(self_closing_group)
        results.append(self_closing_group)
    return results

