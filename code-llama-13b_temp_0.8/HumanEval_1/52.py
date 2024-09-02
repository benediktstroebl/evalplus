from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    # Hint 1: You can use two stacks, one for keeping track of the open parentheses and one for storing
    # the result strings. Whenever you encounter a close parentheses push the current result string
    # (initially empty) to the result stack and pop the stack till the corresponding open parentheses is found.
    # Now add the balanced parentheses to the string which you're keeping track in the result stack.
    # For any other kind of brace, just push it to the stack.
    # Hint 2: You don't need to actually separate the parentheses from the string. Keeping track of the indices of
    # open parentheses is enough.

    result, open_parens = [], []
    for index, paren in enumerate(paren_string):
        if paren == "(":
            open_parens.append(index)
        elif paren == ")":
            if open_parens[-1] == index - 1 and len(open_parens) > 1:
                open_parens.pop()
                result[-1] += ")"
            elif open_parens:
                open_parens.pop()
                result.append(")")
    return result

