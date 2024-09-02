from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    # Iterate through the string with two pointers. The rightmost and leftmost parens
    # don't need to be visited, because anything contained completely within another
    # paren group is contained in the parent group. We start at the rightmost paren and
    # move left until we reach the leftmost paren. Then we move right until we reach the next
    # leftmost paren. Continue this process until the string is empty.
    left, right = 0, len(paren_string) - 1
    result = []
    while left <= right:
        # Ignore any spaces
        curr = paren_string[left:right + 1].replace(' ', '')
        # If we have an open paren, add the current group to the result and move to the left
        if '(' in curr:
            result.append(curr)
            left += 1
        # If we have a closed paren, add the current group to the result and move right
        elif ')' in curr:
            result.append(curr)
            right -= 1
        # When we get to the next leftmost paren, we are done. The current group is now the last in the result
        # and we can begin a new group.
        else:
            result.append(curr)
            left = right + 1

    return result

