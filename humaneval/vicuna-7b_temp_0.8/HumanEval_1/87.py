from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    def reconstruct_group(open_brace: str) -> str:
        """
        This function takes an open brace and reconstructs the group of parentheses that it is a part of.
        The output is a string with the open brace followed by all the
        """
        if open_brace in paren_string:
            left, right = reconstruct_group(paren_string[open_brace:])
            return left + ")" + right
        else:
            return ")"

    def reconstruct_group_rec(open_brace: str) -> List[str]:
        if open_brace in paren_string:
            left, right = reconstruct_group(paren_string[open_brace:])
            return [reconstruct_group_rec(left), reconstruct_group_rec(right)]
        else:
            return [reconstruct_group_rec(open_brace)]

    def reconstruct_group_seq(paren_string: str) -> List[str]:
        if not paren_string:
            return []
        if paren_string[0] == '(':
            return [reconstruct_group_seq(paren_string[1:])]
        else:
            left, right = reconstruct_group_seq(paren_string[1:])
            return left + ")" + reconstruct_group_seq(paren_string[1:])

    groups = reconstruct_group_seq(paren_string)
    return groups

example = "( ) (( )) (( )( ))"
