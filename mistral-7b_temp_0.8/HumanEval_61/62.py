

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
    # TODO: Write your solution here
    # Hint: Use a while loop to add to a list
    brackets = []
    for char in brackets:
        if char == "(":
            brackets.append(")")
        elif char == ")":
            brackets.append("(")
    return len(brackets) == 0
