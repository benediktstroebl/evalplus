from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    # Create two stacks for open braces and close braces
    open_stacks = []
    close_stacks = []
    # Create two pointers for open and close brackets
    open_pointer = 0
    close_pointer = 0
    # Create a list to store result
    result = []
    # Iterate through the string
    for i in range(len(paren_string)):
        # If open bracket, push to open_stacks
        if paren_string[i] == '(':
            open_stacks.append('(')
        # If close bracket, pop from open_stacks, combine with close_stacks and push to result
        elif paren_string[i] == ')':
            # If open_stacks empty, open bracket is irrelevant
            if len(open_stacks) == 0:
                continue
            # If parenthesis already closed, open bracket is irrelevant
            elif len(close_stacks) == 0:
                continue
            # If open bracket, pop, combine and push to result
            else:
                top = open_stacks.pop()
                close_stacks.pop()
                combination = top + close_stacks.pop()
                result.append(combination)
    # If open_stacks is not empty, pop all elements and push to result
    if len(open_stacks) != 0:
        while len(open_stacks) != 0:
            result.append(open_stacks.pop())
    # If close_stacks is not empty, push all elements to result
    if len(close_stacks) != 0:
        while len(close_stacks) != 0:
            result.append(close_stacks.pop())
    return result

