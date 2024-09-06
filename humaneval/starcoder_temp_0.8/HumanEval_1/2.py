from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    # * use a stack to keep track of open parentheses
    # * iterate through string, add to stack when you encounter an open parens
    # * when you encounter a close paren, check if the stack is empty. if it is, then add the close paren to the stack
    #   this means you have an unbalanced parens group
    # * if the stack is not empty, then pop the last char off the stack. this char is the last open parens
    #   that is balanced. append that char to the result string. then append the current close parens.
    # * this process continues until the stack is empty or until you encounter an unbalanced parens group
    # * return the list of strings
    stack = []
    result = []
    for char in paren_string:
        if char == "(":
            stack.append(char)
        else:
            if stack:
                result.append(stack.pop())
                result.append(char)
            else:
                result.append(char)
    return list(map(lambda x: "".join(x), zip(*[iter(result)] * 2)))

