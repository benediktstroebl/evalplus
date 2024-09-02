from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """

    def _find_end_of_paren_group(string: str, start_idx: int) -> int:
        """ Helper function to find the index of the end of a paren group.
        """
        open_brace_count = 1
        for idx in range(start_idx, len(string)):
            if string[idx] == '(':
                open_brace_count += 1
            elif string[idx] == ')':
                open_brace_count -= 1
                if open_brace_count == 0:
                    break
        return idx

    def _separate_paren_group(string: str) -> List[str]:
        """ Helper function to separate paren group.
        """
        paren_groups = []
        idx = 0
        while idx < len(string):
            while idx < len(string) and string[idx] == ' ':
                idx += 1
            if idx < len(string) and string[idx] == '(':
                idx += 1
                end_idx = _find_end_of_paren_group(string, idx)
                paren_groups.append(string[idx:end_idx + 1])
                idx = end_idx + 1
            else:
                idx += 1
        return paren_groups

    return _separate_paren_group(paren_string)

