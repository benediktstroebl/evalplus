

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
    bracket_dict = {"<": ">",
                    ">": "<",
                    "(": ")",
                    ")": "("}
    
    stack = []

    for bracket in brackets:
        if bracket not in bracket_dict:
            return False

        if bracket in "<>":
            stack.append(bracket_dict[bracket])
        
        if bracket == ")":
            if len(stack) == 0:
                return False
            
            if stack.pop() != "(":
                return False

    if len(stack) != 0:
        return False

    return True
