from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    paren_depth = 0
    paren_to_group = {}
    group_to_paren = []

    for i, c in enumerate(paren_string):
        if c == '(':
            if paren_depth == 0:
                paren_depth += 1
                paren_to_group[i] = i
                group_to_paren.append([])
            else:
                paren_to_group[i] = len(group_to_paren) - 1
        elif c == ')':
            paren_depth -= 1
            if paren_depth == 0:
                group_to_paren[-1].append(i)

    result = []
    n = 0
    for group in group_to_paren:
        paren = paren_to_group[group[0]]
        for i in group:
            l = len(group_to_paren[paren])
            new = i - l
            if new < group[0]:
                paren_to_group[new] = paren
            else:
                group_to_paren[paren].append(new)
        if len(group_to_paren[paren]) == 1:
            result.append(paren_string[n:group_to_paren[paren][0]])
            n = group_to_paren[paren][0] + 1
        else:
            result.append(paren_string[n:group_to_paren[paren][0]])
            n = group_to_paren[paren][-1] + 1
    result.append(paren_string[n:])

    return result

