

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
    def count(brackets):
        count = 0
        for b in brackets:
            if b == "(":
                count += 1
            elif b == ")":
                count -= 1
        return count

    def check_bracketing(brackets):
        for i in range(len(brackets) - 1):
            if brackets[i] != brackets[i + 1]:
                return False
        return True

    if count(brackets) % 2 == 0:
        return check_bracketing(brackets)
    else:
        return False
