from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    # HINT: You may want a stack for this
    res = []
    temp = ""
    for char in paren_string:
        if char == "(":
            if temp != "":
                res.append(temp)
                temp = ""
            temp += "("
        elif char == ")":
            temp += ")"
            if temp[0] == "(" and temp[-1] == ")":
                res.append(temp)
                temp = ""
        elif char != " ":
            temp += char
    return res

