from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    parentheses = []
    for i in range(len(paren_string)):
        if paren_string[i] == '(':
            parentheses.append(paren_string[i])
        elif paren_string[i] == ')':
            if len(parentheses) > 0:
                parentheses.pop()
            else:
                parentheses.append(paren_string[i])
        else:
            parentheses.append(paren_string[i])

    result = []
    for i in range(len(parentheses)):
        if parentheses[i] == '(':
            new_result = []
            for j in range(i+1, len(parentheses)):
                if parentheses[j] == ')':
                    new_result.append(parentheses[i+1:j])
                    break
            result.append(''.join(new_result))

    return result
