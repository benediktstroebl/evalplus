from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    output_list = []
    paren_string = paren_string.replace(" ", "")
    paren_list = [x for x in paren_string]
    while paren_list:
        current_paren = []
        for element in paren_list:
            if element == "(":
                paren_list.pop(0)
                current_paren.append("(")
                break
            elif element == ")":
                current_paren.append(element)
                output_list.append("".join(current_paren))
                paren_list.pop(0)
                current_paren = []
                break
        else:
            break
    return output_list

