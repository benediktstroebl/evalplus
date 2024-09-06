from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    def left_to_right(string):
        return ''.join(re.findall(r'\([^()]*\)', string))

    def right_to_left(string):
        return ''.join(re.findall(r'\)([^()]*)\)(?!\()', string))

    left_paren_count = 0
    right_paren_count = 0
    result = []
    for char in paren_string:
        if char == '(':
            left_paren_count += 1
        elif char == ')':
            right_paren_count += 1
        elif char == '(' and left_paren_count % 2 == 0:
            result.append(paren_string[left_paren_count-1:])
            left_paren_count -= 1
        elif char == ')':
            if left_paren_count % 2 == 0:
                result.append('')
            left_paren_count += 1
        else:
            result.append(char)

    return result