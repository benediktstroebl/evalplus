

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
    characters = []
    for character in brackets:
        if character == "<":
            characters.append(character)
        elif character == ">":
            if len(characters) == 0:
                return False
            else:
                popped = characters.pop()
                if popped != "<" and popped != ">":
                    return False
    return len(characters) == 0
