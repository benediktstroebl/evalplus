from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    if paren_string is None or len(paren_string) == 0:
        return []

    paren_groups = []

    current_group = []
    n = 0
    i = 0
    while i < len(paren_string):
        if paren_string[i] == "(":
            current_group.append(paren_string[i])
            n += 1
            i+=1
        elif paren_string[i] == ")":
            current_group.append(paren_string[i])
            n -= 1
            i+=1
        elif paren_string[i] == " ":
            i+=1
        else:
            try:
                while paren_string[i] == ")":
                    x = paren_string[i+1]
                    if x == "(":
                        n += 1
                    else:
                        n -= 1
                    i += 2
            # the current_group was not a balanced parenthesis group. Append it to the output.
            except IndexError:
                if n != 0 and current_group:
                    paren_groups.append("".join(current_group))
                    current_group = []
            # the current_group was a balanced parenthesis group. Save it and start over.
            else:
                if n == 0:
                    paren_groups.append("".join(current_group))
                current_group = []
            # proceed to the next character in paren_string
            i += 1

    if current_group:
        paren_groups.append("".join(current_group))

    return paren_groups
