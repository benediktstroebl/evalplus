from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    def _extract_group(open_brace_index: int, close_brace_index: int, string: str) -> str:
        """ Recursive function to extract the group between open and close braces.
        """
        if close_brace_index - open_brace_index == 1:
            return string.split(open_brace_index, maxsplit=open_brace_index)[0]
        else:
            return _extract_group(open_brace_index + 1, close_brace_index, string) + _extract_group(open_brace_index, close_brace_index - 1, string)

    return [ _extract_group(i + 1, j, paren_string) for i, j in enumerate(zip(re.finditer(r'\((.+)\)', paren_string), [i for i, char in enumerate(paren_string) if char == '('])))]
