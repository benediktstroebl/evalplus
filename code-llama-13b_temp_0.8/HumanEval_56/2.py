

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

    # Hint: Use a stack.

    if brackets == '':
        return True
    if len(brackets) % 2 != 0:
        return False
    else:
        stack = Stack()
        for i in range(len(brackets)):
            if brackets[i] == '<':
                stack.push('<')
            elif brackets[i] == '>':
                if stack.is_empty():
                    return False
                if stack.pop() != '<':
                    return False
        return stack.is_empty()

