

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
    # Helper function that returns True if the string is balanced.
    # A string is balanced if all of its brackets are correctly interlaced.
    def balanced(brackets):
        result = True
        left = 0
        right = 0
        for i in range(len(brackets)):
            if brackets[i] == '<':
                left += 1
            elif brackets[i] == '>':
                right += 1
            if left < right:
                result = False
        return result

    # Implement correct_bracketing using the balanced helper function.
    return balanced(brackets)

