from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    result = []
    result_set = ""
    new_start = 0

    for i, char in enumerate(paren_string):
        if char == "(":
            result_set += "("
            if i + 1 >= len(paren_string) or paren_string[i + 1] == ")":
                new_start = i + 2
        elif char == ")":
            result_set += ")"
            if result_set.count("(") == result_set.count(")"):
                result.append(result_set)
                result_set = ""
                if i + 1 < len(paren_string) and paren_string[i + 1] != ")":
                    new_start = i + 2

    return result

