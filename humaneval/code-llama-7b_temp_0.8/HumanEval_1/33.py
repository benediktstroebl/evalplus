from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    # If the string is empty or it contains just a single parenthesis, the return the string itself
    if not paren_string:
        return [paren_string]

    # check if all paranthesis are balanced
    open_count = 0
    for i, paren in enumerate(paren_string):
        if paren == "(":
            open_count += 1
        elif paren == ")":
            open_count -= 1
        if open_count < 0:
            raise ValueError(
                "Paranthesis are not balanced in the string", paren_string
            )
        # return the result if all paranthesis are balanced
        if open_count == 0 and i == len(paren_string) - 1:
            return [paren_string]

    # if there are nested paranthesis, separate them into separate strings and return the list of those
    # when there is a nested paranthesis, the paranthesis are on either side of the opening paranthesis
    # so the paranthesis to the left of the opening paranthesis is not nested
    result = []
    nested = False
    new_string = ""
    for paren in paren_string:
        if not nested and paren == "(":
            if new_string:
                result.append(new_string)
            new_string = ""
        elif nested and paren == ")":
            nested = False
        elif nested:
            new_string += paren
        elif not nested and paren == ")":
            raise ValueError(
                "Paranthesis are not balanced in the string", paren_string
            )
        elif not nested and paren == "(":
            nested = True
        else:
            new_string += paren

    return result

