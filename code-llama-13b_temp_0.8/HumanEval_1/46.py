from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    # Find first group
    group_count = 0
    paren_index = 0

    # Count opening and closing parens and find first complete group
    while paren_index < len(paren_string):
        paren = paren_string[paren_index]

        if paren == '(':
            group_count += 1
        elif paren == ')':
            group_count -= 1

        if group_count == 0:
            break

        paren_index += 1

    # If no groups found
    if paren_index == 0:
        return []

    # Get the first group
    first_group = paren_string[:paren_index + 1]

    # Remove the first group from string
    paren_string = paren_string[paren_index + 1:]

    # Recursively find the remaining groups
    groups = [first_group]
    groups.extend(separate_paren_groups(paren_string))

    return groups

