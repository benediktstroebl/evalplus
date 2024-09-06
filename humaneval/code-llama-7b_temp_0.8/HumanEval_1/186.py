from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    # your code here
    # Clarification: The question can be rephrased as "To separate a string into words, only consider a substring as a
    # word if that substring is separated by a non-word character"
    # Think of the input string as a big stack of parentheses, starting with the innermost brace.
    # For each opening brace, add a new stack on top of the stack
    # For each closing brace, pop the top stack
    # When a new closing brace is encountered, push the contents of the stack onto a global stack
    # When a stack is empty after popping the last closing brace, join the content of the global stack
    result = []
    stack = []
    global_stack = []
    for paren in paren_string:
        if paren == '(':
            stack.append(paren)
        elif paren == ')':
            stack.pop()
        if not stack:
            result.append("".join(global_stack))
            global_stack.clear()
        else:
            global_stack.append(paren)
    result.append("".join(global_stack))
    return result

