from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    # Your code here
    result = []
    current_str = []
    index = 0
    while index < len(paren_string):
        if (
            paren_string[index] == '('
            and paren_string[index + 1] != ')'
            and len(current_str) == 0
        ):
            # print('Opening {0}'.format(paren_string[index]))
            current_str.append(paren_string[index])
        elif (
            paren_string[index] == ')'
            and paren_string[index - 1] == '('
            and len(current_str) > 0
            and current_str[-1] != '('
        ):
            # print('Closing {0}'.format(paren_string[index]))
            current_str.append(paren_string[index])
        elif (
            paren_string[index] == ')'
            and paren_string[index - 1] == '('
            and len(current_str) > 0
            and current_str[-1] == '('
        ):
            # print('Adding {0} to {1}'.format(paren_string[index], current_str))
            current_str.append(paren_string[index])
        elif (
            paren_string[index] == ')'
            and paren_string[index + 1] == ')'
            and len(current_str) > 0
            and current_str[-1] == '('
        ):
            # print('Adding {0} to {1}'.format(paren_string[index], current_str))
            current_str.append(paren_string[index])
            current_str.append(paren_string[index])
            # print('Closing {0}'.format(current_str))
            result.append(current_str)
            current_str = []
        elif (
            paren_string[index] == '('
            and paren_string[index + 1] != ')'
            and len(current_str) > 0
            and current_str[-1] == '('
        ):
            current_str.append(