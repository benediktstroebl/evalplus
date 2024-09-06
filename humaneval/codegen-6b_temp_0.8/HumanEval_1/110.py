from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    # Start by separating out each group of parentheses
    # we've already handled the last )
    paren_groups = []
    curr_group = []
    for char in paren_string:
        curr_group.append(char)
        if char == ')':
            paren_groups.append(''.join(curr_group))
            curr_group = []
    if curr_group:
        paren_groups.append(''.join(curr_group))

    # Now do the same with the opening and closing parentheses
    opening = []
    closing = []
    for i in range(len(paren_groups)):
        paren_group = paren_groups[i]
        match = closing_paren_match(paren_group)
        if match:
            opening.append(paren_group[:match[0]])
            closing.append(paren_group[match[0]:match[1]])
            paren_groups[i] = paren_group[match[1]:]

        else:
            opening.append(paren_group)

    # Now the rest of the parentheses aren't relevant, so are all of the ones that aren't open or closing
    return list(filter(lambda x: x not in opening and x not in closing, paren_groups))

