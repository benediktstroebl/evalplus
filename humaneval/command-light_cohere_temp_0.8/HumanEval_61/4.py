```python
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
# Example usage:
# Test string with unbalanced brackets
correct_bracketing("(()())")
# Test string with balanced brackets
correct_bracketing("()")
# Test string with mismatched brackets
correct_bracketing(")())")
 ```  This function, `correct_bracketing`, takes a string of opening brackets (`(" and ")) and returns `True` if the brackets are balanced and `False` otherwise. It uses a particular open and close bracket and pushes or pops it into/from a stack to check if the brackets are balanced.