

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
    # your code goes here
    # notice that this function does not return a string
    # it can return a boolean value, or a string of any other type
    brackets = brackets.replace("<", "a").replace(">", "b")
    print(brackets)
    return brackets.count("a") == brackets.count("b")

