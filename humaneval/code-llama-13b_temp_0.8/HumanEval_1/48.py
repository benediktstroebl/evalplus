from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    # Hint: when do you want to add a new group to the result list?
    result = []
    # Hint: What data structure will help you with balancing parentheses?
    stack = []

    # Hint: What should you do when you encounter an open brace?
    for c in paren_string:
        if c == '(':
            stack.append('(')
        elif c == ')':
            # Hint: What should you do when you encounter a close brace?
            if len(stack) > 0:
                stack.pop()
                # Hint: What should you do when you encounter a close brace, but the stack is empty?
                # raise ValueError('Parentheses are not balanced.')
            else:
                result.append(')')
    return result
