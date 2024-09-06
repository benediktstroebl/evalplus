from typing import List
def separate_paren_groups(paren_string: str) -> List[str]:
    """
    Separate groups of nested parentheses into separate strings and return the list of those.

    Args:
        paren_string (str): A string containing multiple groups of nested parentheses.

    Returns:
        List[str]: A list of strings, each representing a separate group of parentheses.

    Example:
        >>> separate_paren_groups('( ) (( )) (( )( ))')
        ['()', '(())', '(()())']
    """

    if not paren_string:
        return []

    # Split the string into individual parentheses groups, ignoring spaces
    paren_groups = paren_string.split(' ')

    # Use a deque (double-ended queue) to efficiently stack and unwind parentheses
    stack = []
    result = []
    for group in paren_groups:
        # Stack open parentheses
        stack.append(group)

        # Unwind until we reach a balanced group (see NOTE below)
        while stack and (group.count('(') - group.count(')') != len(stack) or group == '('):
            result.append('')
            stack.pop()

        # Add the balanced group to the result
        result.append(group)

    return result