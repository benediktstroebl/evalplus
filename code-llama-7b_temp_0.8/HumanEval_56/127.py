

def correct_bracketing(brackets: str):
    """ brackets is a string of "<" and ">".
    return True if every opening bracket has a corresponding closing bracket.

    >>> correct_bracketing("<")
    False
    >>> correct_bracketing("<>")
    True
    >>> correct_bracketing("<<><>>")
    True
    >>> correct_bracketing("><<>")
    False
    """
    brac_stack = []
    brac_open = ['[', '(', '{', '<']
    brac_close = [']', ')', '}', '>']
    for char in brackets:
        if char in brac_open:
            brac_stack.append(char)
        elif char in brac_close:
            pos = brac_close.index(char)
            if ((len(brac_stack) > 0) and
                (brac_open[pos] == brac_stack[len(brac_stack)-1])):
                brac_stack.pop()
            else:
                return False
    return len(brac_stack) == 0



