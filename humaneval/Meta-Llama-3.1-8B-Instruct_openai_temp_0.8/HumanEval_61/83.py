```python
def correct_bracketing(brackets: str) -> bool:
    """
    Checks if a string of "(" and ")" has correct bracketing.
    
    Args:
        brackets (str): A string containing only "(" and ")".
    
    Returns:
        bool: True if every opening bracket has a corresponding closing bracket, False otherwise.
    """
    stack = []  # Initialize an empty stack
    
    for bracket in brackets:
        if bracket == "(":  # If the bracket is an opening bracket, push it to the stack
            stack.append(bracket)
        elif bracket == ")":  # If the bracket is a closing bracket
            if not stack:  # If the stack is empty, return False (no corresponding opening bracket)
                return False
            stack.pop()  # If the stack is not empty, pop the opening bracket

    return not stack  # After iterating over all brackets, return True if the stack is empty (correct bracketing)

# Test cases
print(correct_bracketing("("))  # False
print(correct_bracketing("()"))  # True
print(correct_bracketing("(()())"))  # True
print(correct_bracketing(")(("))  # False
print(correct_bracketing(")(()") and correct_bracketing("))"))  # False
```

This script defines a function `correct_bracketing` that takes a string of "(" and ")" as input and returns True if every opening bracket has a corresponding closing bracket, and False otherwise. The function uses a stack to keep track of the opening brackets and checks if every closing bracket has a corresponding opening bracket. The test cases are included in the script to demonstrate the function's correctness.