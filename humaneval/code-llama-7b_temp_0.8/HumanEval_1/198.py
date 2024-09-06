from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    # The idea is to match the pair of parentheses by their indices.
    # If we don't find a pair of parentheses, we will move on the next character.
    # If we find a pair of parentheses, we will move to the next character after the ending one.
    # If we have already visited a pair of parentheses, we will start from the next opening brace.
    # For example, '(()())' will be converted to a list of pairs [0, 0, 1, 1, 1, 2, 2], where [0, 1] is the
    # first pair of parentheses, [1, 1] is the second pair of parentheses and so on.
    pairs_stack: List[int] = []
    output: List[str] = []
    for idx, char in enumerate(paren_string):
        if char == '(':
            pairs_stack.append(idx)
        elif char == ')':
            start_idx = pairs_stack.pop()
            end_idx = idx
            output.append(paren_string[start_idx:end_idx + 1])
    return output

