from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    result = []
    left_start = right_end = 0
    left_count = right_count = 0
    for i in range(len(paren_string)):
        if paren_string[i] == "(":
            left_count += 1
            if left_count == 1:
                left_start = i
        elif paren_string[i] == ")":
            right_count += 1
            if right_count == 1:
                right_end = i
        if left_count > 0 and left_count == right_count:
            result.append(paren_string[left_start:right_end + 1].strip())
            left_count = right_count = 0
    return result

