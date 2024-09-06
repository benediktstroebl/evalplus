from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    # code goes here
    """
    Stack is used to track the open parenthesis
    Whenever we encounter an open parenthesis we put that to the stack
    Whenever we encounter a close parenthesis we pop an element from the stack
    and add it to the result string 
    Whenever we encounter a space we keep on popping elements from the stack and adding them to the result string
    until the stack is empty.
    
    """

    stack = []
    result = []
    result_string = ""
    for char in paren_string:
        if char == " ":
            while stack:
                result_string += stack.pop()
            result.append(result_string)
            result_string = ""
        elif char == "(":
            stack.append("(")
        elif char == ")":
            while stack and stack[-1] != "(":
                result_string += stack.pop()
            stack.pop()
            result_string += char
    while stack:
        result_string += stack.pop()
    result.append(result_string)
    return result

