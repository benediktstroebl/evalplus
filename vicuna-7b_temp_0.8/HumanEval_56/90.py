

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
    # Replace all opening brackets with a space, and all closing brackets with a space.
    # This effectively removes all brackets from the string.
    brackets = " " + brackets + " "
    # Split the string into a list of characters.
    brackets_list = brackets.split()
    # Iterate over the list of characters.
    for i in range(0, len(brackets_list)):
        if i % 2 == 0:
            # If the current character is an opening bracket, there must be a corresponding closing bracket.
            if not any(brackets_list[i + 1:]):
                return False
        else:
            # If the current character is a closing bracket, there must be a corresponding opening bracket.
            if not any(brackets_list[:i]):
                return False
    # If we've made it through the entire list without encountering a problem, the bracketing is correct.
    return True