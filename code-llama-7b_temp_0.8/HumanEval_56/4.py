

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
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # This is a simple but slow solution.
    # There is a better solution that uses a stack. #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # 1. We can count the number of "<"s and the number of ">"s.
    # 2. If the number of "<"s is greater than the number of ">"s, we have a ">".
    # 3. If the number of "<"s is less than the number of ">"s, we have a "<".
    # 4. If the number of "<"s is equal to the number of ">"s, we have a match.
    # 5. We perform steps 2-5 recursively until there are no more characters to check.
    # 6. If at the end of our checks the number of "<"s is greater than the number of ">"s, we return False.
    # 7. If at the end of our checks the number of "<"s is less than the number of ">"s, we return False.
    # 8. If at the end of our checks the number of "<"s is equal to the number of ">"s, we return True.

    open_brackets = brackets.count("<")
    close_brackets = brackets.count(">")

    if open_brackets > close_brackets:
        return False
    elif open_brackets < close_brackets:
        return False
    elif open_brackets == close_brackets:
        return True
    elif open_brackets == 0 and close_brackets == 0:
        return True

    return correct_bracketing(brackets[1:])

