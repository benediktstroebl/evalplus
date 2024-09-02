from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    separated_strings: List[str] = []
    string_stack: List[str] = []
    open_braces: List[str] = ["(", "[", "{"]
    close_braces: List[str] = [")", "]", "}"]
    i: int = 0
    in_string = True
    while i < len(paren_string):

        k = paren_string[i]
        if k in open_braces:
            string_stack.append(k)
            i += 1

        elif k in close_braces:
            if not string_stack:
                i += 1
                in_string = False
            elif string_stack[-1] == open_braces[close_braces.index(k)]:
                string_stack.pop()
                i += 1
            else:
                in_string = False

        elif in_string:
            separated_strings.append(paren_string[i])
            i += 1

        else:
            i += 1

    if string_stack:
        in_string = False

    return [s for s in separated_strings if s != ""]

