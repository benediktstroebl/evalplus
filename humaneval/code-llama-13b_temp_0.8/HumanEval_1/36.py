from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """

    # 1. scan for first open paren
    # 2. scan for balanced closing paren
    # 3. if no balanced closing paren, raise error
    # 4. save the group
    # 5. look for another group, starting at the character after the closing paren
    # 6. when no more open parens, return groups

    groups = []
    start = 0

    while True:
        open_paren = paren_string.find("(", start)
        if open_paren == -1:
            return groups
        balanced_paren = 0
        for i in range(open_paren, len(paren_string)):
            if paren_string[i] == "(":
                balanced_paren += 1
            elif paren_string[i] == ")":
                balanced_paren -= 1
            if balanced_paren == 0:
                groups.append(paren_string[open_paren: i + 1])
                start = i + 1
                break
































































































































































































































































