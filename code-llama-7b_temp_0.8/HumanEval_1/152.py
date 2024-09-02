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
    temp = ""

    def push_result(string: str) -> None:
        nonlocal result
        result.append(string)

    stack = []
    for i in paren_string:
        if i == "(":
            stack.append("(")
        elif i == ")":
            if not stack or stack.pop() != "(":
                return []
            if not stack:
                push_result(temp)
                temp = ""
        temp += i
    return result

