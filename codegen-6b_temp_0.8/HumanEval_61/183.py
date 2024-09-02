

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
    
    brackets = list(brackets)
    balanced = True
    while balanced:
        balanced = False
        for i in range(len(brackets)):
            if brackets[i] == '(':
                balanced = True
                balanced = balanced and correct_bracket(brackets, i)
                if not balanced:
                    return balanced
                balanced = balanced and correct_bracket(brackets, i)
                
            elif brackets[i] == ')':
                balanced = True
                balanced = balanced and correct_bracket(brackets, i)
                if not balanced:
                    return balanced
    return balanced
    