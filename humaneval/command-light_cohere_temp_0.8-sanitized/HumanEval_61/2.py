def correct_bracketing(brackets: str):
    """
    Checks whether a string of "(" and ")" has a balanced bracket structure
    Returns: boolean indicating balance
    """
    stack = []
    for char in brackets:
        if char == '(':  # push to stack
            stack.push("(")
       
        elif char == ')':  # pop from stack and return
            return True  # matching closing bracket found
    return False