

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
    # split the string of brackets into a list of brackets
    brackets = brackets.split("<>")
    
    # count the number of opening brackets and the number of closing brackets
    num_opening = 0
    num_closing = 0
    for b in brackets:
        if b == "<":
            num_opening += 1
        else:
            num_closing += 1
    
    # check if the number of opening brackets is equal to the number of closing brackets
    return num_opening == num_closing
