

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
    def _correct_bracketing(brackets):
        for opening, closing in zip(brackets, brackets[1:]+['']):
            if opening != closing:
                return False
        return True
    return _correct_bracketing(brackets)

if __name__ == '__main__':
    print(correct_bracketing("("))
    print(correct_bracketing("()"))
    print(correct_bracketing("(()())"))
    print(correct_bracketing(")(()"))