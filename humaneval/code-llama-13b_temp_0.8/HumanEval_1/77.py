from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    # HINT: you may want a stack to help you separate the groups.
    # - If you find an open brace, push it to the stack
    # - If you find a closed brace, pop the last open brace from the stack, and start a new word
    #   (make sure the stack isn't empty when you do this!)
    # - If the stack is empty and you find a closed brace, raise an error - this shouldn't happen!
    # - If you find a character that's not a brace, add it to the current word
    result: List[str] = []
    word: List[str] = []
    for c in paren_string:
        if c == "(":
            word.append(c)
        elif c == ")":
            word.pop()
            if len(word) == 0:
                result.append("".join(word))
        else:
            word.append(c)
    return result

