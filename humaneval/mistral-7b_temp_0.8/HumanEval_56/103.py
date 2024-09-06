

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
    opening_brackets = "><"
    closing_brackets = "<>"

    brackets_stack = []
    for i in range(len(brackets)):
        if brackets[i] in opening_brackets:
            brackets_stack.append(brackets[i])
        elif brackets[i] in closing_brackets:
            if len(brackets_stack) == 0:
                return False
            if brackets_stack[-1] == brackets[i].replace("<", ""):
                brackets_stack.pop()
            else:
                return False

    return len(brackets_stack) == 0

