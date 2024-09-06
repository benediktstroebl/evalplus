

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
    
    opening_brackets_index = []
    
    for i, char in enumerate(brackets):
        if char == "(":
            opening_brackets_index.append(i)
    
    closing_brackets_index = []
    
    for i, char in enumerate(brackets):
        if char == ")":
            closing_brackets_index.append(i)
    
    if len(opening_brackets_index) != len(closing_brackets_index):
        return False
    
    for i in range(len(opening_brackets_index)):
        if opening_brackets_index[i] != closing_brackets_index[i] - 1:
            return False
    
    return True
    