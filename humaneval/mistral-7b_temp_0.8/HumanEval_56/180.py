

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
    # Replace all "<" with "[" and all ">" with "]"
    replaced = brackets.replace("<", "[")
    replaced = replaced.replace(">", "]")

    # Reverse the string
    reversed = replaced[::-1]

    # Compare the reversed string with the original string
    return replaced == reversed

