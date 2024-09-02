from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    final_list = []
    current_list = None
    loop_num = 0
    for i in range(0, len(paren_string)):
        if paren_string[i] == '(':
            if loop_num == 0:
                current_list = [paren_string[i]]
                loop_num += 1
            else:
                current_list.append(paren_string[i])
        elif paren_string[i] == ')':
            if current_list is not None:
                if loop_num == 0:
                    final_list.append(''.join(current_list))
                else:
                    final_list.append(''.join(current_list))
                    loop_num -= 1
            else:
                pass
        elif paren_string[i] == ' ':
            pass
        else:
            if current_list is not None:
                current_list.append(paren_string[i])
            else:
                current_list = [paren_string[i]]
                loop_num += 1
    return final_list

