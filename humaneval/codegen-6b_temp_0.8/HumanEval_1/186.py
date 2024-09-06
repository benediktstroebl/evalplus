from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    index_pairs = []
    for i, letter in enumerate(paren_string):
        if letter == '(':
            index_pairs.append(i)
        elif letter == ')':
            if index_pairs == [] or index_pairs[-1] < i:
                index_pairs.append(i)

    for start, end in zip(index_pairs, index_pairs[1:]):
        paren_string = (
            paren_string[:start + 1]
            + paren_string[end:]
            + paren_string[start:end]
        )

    return paren_string.split('()')

