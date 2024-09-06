

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

    # TIP: as you read the strings, which one do you need to remember?

    # TIP: keep track of the number of opening brackets you've seen so far.

    # TIP: when you find a closing bracket, you know how many opening brackets
    # there were at that point.

    # TIP: when you're done reading the string, if there are an odd number of
    # brackets remaining, the string is not properly bracketed.

    # TIP: when you're done reading the string, if there are an even number of
    # brackets remaining, the string is properly bracketed.

    # BEGIN PROBLEM 5
    brackets_count = 0
    for c in brackets:
        if c == '>':
            brackets_count -= 1
        else:
            brackets_count += 1
    return brackets_count == 0
    # END PROBLEM 5
