

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
    assert isinstance(brackets, str), f'brackets should be a str, not a {type(brackets)}'
    assert brackets.count('(') == brackets.count(')'), f'not every opening bracket has a corresponding closing bracket: {brackets}'

    if len(brackets) == 1:
        return False

    for i in range(1, len(brackets)):
        if brackets[i-1] == '(' and brackets[i] == ')':
            continue
        if brackets[i-1] == ')' and brackets[i] == '(':
            continue
        else:
            return False
    return True

