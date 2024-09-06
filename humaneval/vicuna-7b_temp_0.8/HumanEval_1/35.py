from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    paren_count = Counter()

    for char in paren_string:
        if char == '(':
            paren_count['('] += 1
        elif char == ')':
            paren_count[')']] -= 1
        elif paren_count['('] == paren_count[')']]:
            paren_count[char] += 1
            if paren_count[char] == 1:
                yield f"({paren_count[char]})"

    if paren_count['('] != 0 or paren_count[')']] != 0:
        yield f"({paren_count['(']})"

    for char in paren_string:
        if char == '(':
            paren_count['('] += 1
        elif char == ')':
            paren_count[')']] -= 1
        elif paren_count['('] == paren_count[')']:
            paren_count[char] += 1
            if paren_count[char] == 1:
                yield f"({paren_count[char]})"

    if paren_count['('] != 0 or paren_count[')']] != 0:
        yield f"({paren_count[')']})"
