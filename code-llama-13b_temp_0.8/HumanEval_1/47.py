from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    if len(paren_string) == 0:
        return []
    output = []
    i = 0
    while i < len(paren_string):
        if paren_string[i] == "(":
            counter = 0
            while counter >= 0:
                if paren_string[i] == "(":
                    counter += 1
                if paren_string[i] == ")":
                    counter -= 1
                i += 1
                if i >= len(paren_string):
                    break
            i -= 1
            output.append(paren_string[j:i + 1].replace(" ", ""))
            j = i + 1
        i += 1
    return output

