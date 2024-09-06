

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
    bracket_stack = []
    
    for i in range(len(brackets)):
        if brackets[i] == "(":
            bracket_stack.append(brackets[i])
            
        if brackets[i] == ")":
            if not bracket_stack:
                return False
            bracket_stack.pop()
    
    return not bracket_stack
    
import doctest    