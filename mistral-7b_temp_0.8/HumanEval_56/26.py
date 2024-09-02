

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
    opening_brackets = "()[]{}"
    bracket_dict = {
        "(": ")",
        "[": "]",
        "{": "}",
    }

    # Each bracket will be counted as a 1.
    # Opening bracket: 1
    # Closing bracket: -1

    # As long as the closing bracket is encountered, count will be 0.
    # Otherwise, the brackets are not correctly bracketed.
    count = 0

    for bracket in brackets:
        # If the bracket is opening bracket
        if bracket in opening_brackets:
            # Increment the count by 1
            count += 1
        else:
            # If the bracket is closing bracket
            # Decrement the count by 1
            count -= 1

    return count == 0

