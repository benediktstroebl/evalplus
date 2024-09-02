

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
    # count = 0
    # for char in brackets:
    #     if char == '<':
    #         count += 1
    #     elif char == '>':
    #         count -= 1
    #     if count < 0:
    #         return False
    # return count == 0

    # remember the index of the left bracket that we haven't seen a corresponding right bracket yet.
    # If we reach the end, and there are still unmatched left brackets, return false.
    # If we encounter a right bracket, then it matches the last unmatched left bracket.
    #   remove it from the stack
    #   ...if there's still more left brackets, continue
    # if we reach the end and there are no unmatched brackets, then it's correct
    stack = []
    for i in range(len(brackets)):
        if brackets[i] == '<':
            stack.append(i)
        elif brackets[i] == '>':
            if len(stack) > 0:
                stack.pop()
            else:
                return False
    return len(stack) == 0


