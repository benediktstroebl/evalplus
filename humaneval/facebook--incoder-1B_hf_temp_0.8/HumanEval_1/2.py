from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    paren_string = paren_string.strip()
    paren_pairs = [x.split("(") for x in paren_string.split(" ")]
    paren_groups = [[] for _ in paren_pairs]

    i = 0
    for paren_pair in paren_pairs:
        paren_groups[i].append(paren_pair[0])

        for paren in paren_pair[1:]:
            if not paren:
                paren_groups[i].append("")
            else:
                paren_groups[i].append(paren)

        i += 1

    return paren_groups

