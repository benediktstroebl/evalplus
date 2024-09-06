from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    #  The idea is to use a stack to store the elements in the current nesting level.
    #  The first element in the stack is the one we are adding to.
    #  We are going to start by iterating through a copy of the string.
    #  Skip the whitespace as there should only be spaces between opening and closing parentheses.
    #  If we see an open parenthesis, we add it to the stack.
    #  If we see a close parenthesis and the stack is empty, we know the end of the parentheses has been reached
    #  and we add the sub-string to the result list.
    #  In the process, we make sure we don't add anything to the stack when we see a closed parenthesis
    #  that belongs to the current nesting level.
    stack = []
    all_separated_parens = []
    for i in range(len(paren_string) - 1, -1, -1):
        char = paren_string[i]
        if char != ' ':
            if char == '(':
                stack.append(char)
            elif char == ')':
                if len(stack) == 0:
                    #  The stack is empty, there is no matching element in the original string.
                    #  So add the unpaired closing parenthesis to the result list and move on.
                    all_separated_parens.append(char)
                else:
                    #  We know we are dealing with an open parenthesis.
                    #  Pop the stack until we see an open parenthesis with the same nesting level.
                    while len(stack) > 0 and stack[-1] != '(':
                        #  Add the current chain to the result list.
                        all_separated_parens.append(stack.pop())
                    stack.pop()
    all_separated_parens.reverse()
    return all_separated_parens
