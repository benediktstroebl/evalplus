from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """

    separating_pairs = []
    closing_pairs = {'}': '{', ')': '(', ']': '['}
    opening_pairs = {x: y for y, x in closing_pairs.items()}

    pair_stack = []
    for char in paren_string:
        if char in opening_pairs:
            pair_stack.append(char)

        elif char in closing_pairs:
            if not pair_stack or closing_pairs[char] != pair_stack[-1]:
                return []
            pair_stack.pop()

    # If pair_stack is empty, all parentheses have been balanced and processed.
    if not pair_stack:
        separating_pairs = [''.join(pair_stack) for pair_stack in zip(opening_pairs.values(), pair_stack[::-1])]
    return separating_pairs

