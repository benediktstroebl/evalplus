

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
    # 1. keep a counter that counts the number of open brackets
    # 2. if the input is "" or "()" return True
    # 3. decrement the counter when we see a close bracket
    # 4. increment the counter when we see an open bracket
    # 5. when we are at the end of the string and the counter is 0, then return True
    # 6. else return False

    # STRETCH GOAL
    # make sure that the brackets are balanced (i.e., no extra "(" or ")" characters)

    if len(brackets) == 0 or brackets == "()":
        return True
    counter = 0
    for char in brackets:
        if char == "(":
            counter += 1
        elif char == ")":
            counter -= 1

    return counter == 0


