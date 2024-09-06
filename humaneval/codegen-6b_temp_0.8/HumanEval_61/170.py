

def correct_bracketing(brackets: str):
    """ brackets is a string of "(" and ")".
    return True if every opening bracket has a corresponding closing bracket.

    >>> correct_bracketing("(")
    False
    >>> correct_bracketing("()")
    True
    >>> correct_bracketing("(()())")
    True
    >>> correct_bracketing(")(()")
    False
    """
    # clean up the brackets
    brackets = brackets.replace('()','')
    # make it easier to see if there is a closing bracket
    brackets = brackets.replace('(', '()-')
    brackets = brackets.replace(')', ')()')

    stack = []

    for char in brackets:
        if char == '(':
            stack.append(char)
        elif char == ')':
            if not stack:
                return False
            elif stack.pop() != '(':
                return False

    return len(stack) == 0

