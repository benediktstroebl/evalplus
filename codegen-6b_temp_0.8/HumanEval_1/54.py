from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    paren_stack = []
    result_list = []
    opened_parentheses_count = 0
    for character in paren_string:
        if character == "(":
            opened_parentheses_count += 1
            paren_stack.append(character)
        elif character == ")":
            opened_parentheses_count -= 1
            if len(paren_stack) == 0:
                result_list.append("")
            else:
                paren_stack.pop()
        elif character == " ":
            pass
        else:
            if len(paren_stack) == 0:
                result_list.append(character)
            else:
                # This will never happen
                raise Exception("Stack is not empty and letter is not a closing paren")
    if opened_parentheses_count != 0:
        raise Exception("No closing parenthesis for total {}".format(opened_parentheses_count))
    return result_list

