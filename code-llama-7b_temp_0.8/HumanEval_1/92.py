from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    # pre-condition: if not any(i in paren_string for i in '()')
    # then paren_string is a single string without brackets
    # post-condition: return a list of individual strings representing
    # each separate paren group
    if not paren_string:
        return []
    if paren_string.count('(') != paren_string.count(')'):
        return []
    paren_string = paren_string.replace(' ', '')
    if ')' in paren_string and '(' not in paren_string:
        return [paren_string]
    if paren_string[0] != '(':
        return []
    if paren_string[len(paren_string) - 1] != ')':
        return []

    paren_string_list = []
    i = 0
    while i < len(paren_string):
        if paren_string[i] == '(':
            end_ind = 0
            for j in range(i + 1, len(paren_string)):
                end_ind = j
                if paren_string[j] == '(':
                    break
                elif paren_string[j] == ')':
                    end_ind = j
                    break
            if end_ind == i + 1:
                paren_string_list.append(paren_string[i:j + 1])
                i = j + 1
            else:
                paren_string_list.append(paren_string[i:end_ind])
                i = end_ind
        else:
            i += 1
    return paren_string_list

