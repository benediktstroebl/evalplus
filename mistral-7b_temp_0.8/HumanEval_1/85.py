from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    opening_paren = "([{"
    closing_paren = ")]}"
    output_list = []
    current_group = ""
    for index, character in enumerate(paren_string):
        if character in opening_paren:
            current_group += character
        elif character in closing_paren:
            if current_group == "":
                return "Illegal Parens"
            current_group += character
            if current_group[0] == "(" and current_group[-1] == ")":
                output_list.append(current_group)
                current_group = ""
            else:
                current_group = current_group[:-1]
    if current_group != "":
        return "Illegal Parens"
    return output_list

