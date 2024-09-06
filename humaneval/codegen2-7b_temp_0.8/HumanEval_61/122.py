

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
    brackets = brackets.replace("(", "")
    brackets = brackets.replace(")", "")
    if brackets == "":
        return True
    else:
        stack = list(brackets)
        for i in range(len(brackets)):
            if stack[-1] == "(":
                stack.pop()
            else:
                return False
        return True
