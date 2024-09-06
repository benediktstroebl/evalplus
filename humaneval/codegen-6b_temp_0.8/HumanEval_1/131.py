from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    paren_list = []
    num_loops = 0
    i = 0
    while (num_loops < len(paren_string)):
        paren_list.append(paren_string[i:i + 3])
        i += 3
        num_loops += 1

    paren_list = [paren for paren in paren_list if len(paren) == 3]
    paren_list = list(reversed(sorted(list(set(paren_list)), key=len)))
    for i in range(len(paren_list)):
        if i % 2 == 0:
            paren_list[i] = paren_list[i][1:-1]

    return paren_list

