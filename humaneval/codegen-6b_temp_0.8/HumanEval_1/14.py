from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    open_braces = '([{'
    bracket_count = {'(': 0, ')': 0, '[' : 0, ']': 0, '{': 0, '}': 0}
    new_paren_string = ''
    paren_groups = []
    for char in paren_string:
        if char in open_braces:
            bracket_count[char] += 1
        elif char == ')':
            bracket_count[char] -= 1
        elif char == '}':
            bracket_count[char] -= 1
        elif char == ']':
            bracket_count[char] -= 1
        elif char == '}':
            bracket_count[char] -= 1
        if bracket_count[char] == 0:
            if char == ')':
                new_paren_string += ')'
            elif char == '}':
                new_paren_string += '}'
            elif char == ']':
                new_paren_string += ']'
            elif char == '{':
                new_paren_string += '}'
            bracket_count[char] = 0
        else:
            new_paren_string += char

        if len(new_paren_string) > 0 and new_paren_string[-1] in open_braces:
            new_paren_string = new_paren_string[:-1]

    paren_groups.append(new_paren_string)
    # print(paren_groups)
    return(paren_groups)

