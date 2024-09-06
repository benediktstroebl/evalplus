from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    def count_open_parens(s):
        count = 0
        for c in s:
            if c == '(':
                count += 1
            elif c == ')':
                count -= 1
        return count

    def process_group(open_parens, s):
        if count_open_parens(s) == 0:
            yield s
        else:
            for i in range(1, len(s)):
                for open_paren_count in range(1, count_open_parens(s[:i]) + 1):
                    for j in range(open_paren_count):
                        yield s[:i]
                        yield '(' * (open_paren_count - j - 1) + s[i] + ')' * (count_open_parens(s) - open_paren_count + j)
                yield ')' * (count_open_parens(s) - open_paren_count + i)

    open_parens = 0
    for i in range(len(paren_string)):
        for j in process_group(open_parens, paren_string[:i]):
            yield ''.join(j)
        open_parens = 0
    for i in range(len(paren_string)):
        if count_open_parens(paren_string) > 0:
            for j in process_group(open_parens, paren_string[i:]):
                yield ''.join(j)
