from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    # getting rid of all the spaces
    paren_string = paren_string.replace(" ", "")
    # stack to keep track of the unclosed parantheses
    parens_stack = []
    # list to keep all the finished groups
    groups = []

    # iterate over the string
    for char in paren_string:
        if char == '(':
            # found an open paren
            parens_stack.append('(')
        elif char == ')':
            # found a close paren
            if len(parens_stack) == 0:
                # open paren not found, so we need to create a new group
                group = ""
            else:
                # open paren found, so we need to add this close paren to the current group
                group = parens_stack.pop()

            # add the group to the groups list
            groups.append(group + ')')

        else:
            # found a character other than '(' or ')'
            if len(parens_stack) == 0:
                # open paren not found, so we need to create a new group
                group = ""
            else:
                # open paren found, so we need to add this character to the current group
                group = parens_stack.pop()

            # add this character to the group
            group += char

            # add the group to the stack
            parens_stack.append(group)

    # return all the groups
    return groups

