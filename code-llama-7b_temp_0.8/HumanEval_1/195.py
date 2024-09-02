from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """

    def separate_paren_groups_helper(string: str, start: int) -> List[str]:
        if not string:
            return [string]

        stack = []
        for i, char in enumerate(string[start:]):
            if char == "(":
                stack.append(i + start)
            elif char == ")":
                if stack:
                    start_of_group = stack.pop()
                    return [
                        separate_paren_groups_helper(string, start)[0],
                        separate_paren_groups_helper(string, start_of_group + 1)[0],
                    ]
                else:
                    return [string[start:]]

    return separate_paren_groups_helper(paren_string, 0)

