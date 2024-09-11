```python
def correct_bracketing(brackets: str) -> bool:
    """
    Checks if every opening bracket has a corresponding closing bracket.

    Args:
    brackets (str): A string of "<" and ">".

    Returns:
    bool: True if every opening bracket has a corresponding closing bracket, False otherwise.

    >>> correct_bracketing("<")
    False
    >>> correct_bracketing("<>")
    True
    >>> correct_bracketing("<<><>>")
    True
    >>> correct_bracketing("><<>")
    False
    """
    # Initialize a stack to keep track of opening brackets
    stack = []
    
    # Iterate over each character in the string
    for bracket in brackets:
        # If the bracket is an opening bracket, push it onto the stack
        if bracket == "<":
            stack.append(bracket)
        # If the bracket is a closing bracket
        elif bracket == ">":
            # If the stack is empty, there's no corresponding opening bracket, so return False
            if not stack:
                return False
            # If the stack is not empty, pop the opening bracket from the stack
            else:
                stack.pop()
    
    # If the stack is empty after iterating over the entire string, every opening bracket had a corresponding closing bracket, so return True
    # If the stack is not empty, there were opening brackets with no corresponding closing brackets, so return False
    return not stack

# Test the function
print(correct_bracketing("<"))  # Should print: False
print(correct_bracketing("<>"))  # Should print: True
print(correct_bracketing("<<><>>"))  # Should print: True
print(correct_bracketing("><<>"))  # Should print: False
```

This script defines a function `correct_bracketing` that takes a string of "<" and ">" as input and returns `True` if every opening bracket has a corresponding closing bracket, and `False` otherwise. The function uses a stack to keep track of opening brackets and iterates over each character in the input string. If it encounters an opening bracket, it pushes it onto the stack. If it encounters a closing bracket, it checks if the stack is empty (in which case there's no corresponding opening bracket, so it returns `False`) or pops the opening bracket from the stack. After iterating over the entire string, it checks if the stack is empty (in which case every opening bracket had a corresponding closing bracket, so it returns `True`) or not (in which case there were opening brackets with no corresponding closing brackets, so it returns `False`). The script also includes test cases to verify the function's correctness.