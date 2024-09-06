

def correct_bracketing(brackets: str):
    """ brackets is a string of "(" and ")".
    return True if every opening bracket has a corresponding closing bracket.

    >>> correct_bracketing("(")
    False
    >>> correct_bracketing("()")
    True
    >>> correct_bracketing("(()())")
    True
    >>> correct_bracketing(")(()")
    False
    """

    # a. Write your code here
    # using a while loop to traverse the string
    # if the current character is "("
    # then add 1 to the "openning brackets count"
    # if the current character is ")"
    # then subtract 1 from the "openning brackets count"
    # if the "openning brackets count" becomes 0 then it has been balanced
    # if not then return False

    # b. Replace the line above with your code.
    openning_bracket_count = 0

    for char in brackets:
        if char == "(":
            openning_bracket_count += 1
        elif char == ")":
            openning_bracket_count -= 1
        if openning_bracket_count < 0:
            return False
    if openning_bracket_count == 0:
        return True
    else:
        return False
