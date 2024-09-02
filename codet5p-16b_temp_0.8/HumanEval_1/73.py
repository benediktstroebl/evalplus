from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """

    """ First I build the list of groups by finding the groups of open and closed parentheses in the input string.
    Then I check each group to see if it has balanced open and closed parentheses, and if it does, I append
    it to a new list of separated strings.
    """
    groups = []
    open_paren = []
    closed_paren = []
    for i in range(len(paren_string)):
        if paren_string[i] == "(":
            open_paren.append(i)
        elif paren_string[i] == ")":
            closed_paren.append(i)
    for i in range(len(open_paren)):
        for j in range(len(closed_paren)):
            if open_paren[i] < closed_paren[j]:
                groups.append(paren_string[open_paren[i]:closed_paren[j]+1])
    return groups
    pass

