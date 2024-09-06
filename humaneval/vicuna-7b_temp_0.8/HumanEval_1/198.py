from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    def repl(m: Match) -> str:
        group = m.group(0)
        if group == '(':
            left, right = repl(m), repl(m)
            if left == ')':
                return right
            return left + ')'
        elif group == ')':
            left, right = repl(m), repl(m)
            if left == '(':
                return right
            return left + '('
        else:
            return group

    return [repl(m) for m in re.findall(r'\((.+?)\)(?=\))', paren_string)]
