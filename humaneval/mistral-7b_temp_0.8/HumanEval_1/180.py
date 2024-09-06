from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    assert type(paren_string) is str, "Input should be a string"
    assert len(paren_string) >= 2, "Input string must contain at least two characters"
    assert paren_string[0] in '()', "Input string must contain parentheses"
    assert paren_string[-1] in '()', "Input string must contain parentheses"
    # Your code here
    stack = []
    temp = []
    result = []
    for i in range(len(paren_string)):
        if paren_string[i] in '()':
            if paren_string[i] == '(':
                stack.append(paren_string[i])
            else:
                if len(stack) > 0 and stack[-1] == '(':
                    stack.pop()
                    temp.append(paren_string[i])
                else:
                    temp.append(paren_string[i])
                    break
        else:
            temp.append(paren_string[i])
        if i == len(paren_string) -
