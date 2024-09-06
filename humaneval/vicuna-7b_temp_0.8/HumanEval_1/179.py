from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    def _find_open_parentheses(s: str) -> List[int]:
        # start = 0, end = 0
        end = 0
        open_parens = []
        for i in range(len(s)):
            if s[i] == '(':
                end = i
            elif s[i] == ')':
                end = i + 1
                open_parens.append(end)
                end = i + 1
            elif s[i] == ' ':
                end = i
        # Append any remaining open parentheses
        open_parens.append(end)
        return open_parens

    def _process_pair(i: int, open_parens: List[int]) -> str:
        # Check if the current pair is closed (i.e., the closing brace is at a lower index)
        if i + 1 < len(s) and s[i + 1] == ')' and s[i + 2] == '(':
            return s[i:i + 2]
        # If it's not closed, append it to the list of unpaired open parentheses
        open_parens[open_parens.index(i) + 1] = i + 1
        return ''

    def _consume_open_parens(open_parens: List[int], i: int) -> bool:
        # Check if there are any more open parentheses to consume
        if i < len(open_parens):
            return True
        return False

    def _remove_unpaired_open_parens() -> None:
        # Find and remove any unpaired open parentheses
        for i, j in enumerate(open_parens):
            if not _consume_open_parens(open_parens, i):
                open_parens[j] = i

    open_parens = _find_open_parentheses(paren_string)
    result = []
    i = 0
    while i < len(open_parens):
        if _consume_open_parens(open_parens, i):
            result.append(_process_pair(i
