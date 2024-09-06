

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

    brackets = brackets.strip()
    # your code here
    brackets_list = list(brackets)
    number_of_open = 0
    for i in brackets_list:
        if i == "(":
            number_of_open += 1
        if i == ")":
            number_of_open -= 1
            if number_of_open < 0:
                return False

    if number_of_open == 0:
        return True
    else:
        return False
