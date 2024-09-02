

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
    
    # Open brackets:
    # {"<": ">", "<>": ">"}
    # Closed brackets:
    # {"<": ">", "<>" : ">"}
    bracket_map = {"<": ">", "<>": ">"}

    if "<>" in brackets:
        print("ERROR")

    if brackets in bracket_map:
        return False

    bracket_stack = []

    for bracket in brackets:
        #print(bracket)
        if bracket == "<":   
            bracket_stack.append(bracket)
        else:
            if bracket == ">":
                if len(bracket_stack) == 0:
                    return False
                if bracket_stack[-1] == bracket_map[bracket_stack[-1]]:
                    bracket_stack.pop()
                else:
                    return False

    return True if len(bracket_stack) == 0 else False

