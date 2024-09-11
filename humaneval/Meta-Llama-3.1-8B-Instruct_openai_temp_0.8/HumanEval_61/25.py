```python
def correct_bracketing(brackets: str):
    """returns True if every opening bracket has a corresponding closing bracket"""
    stack = []  # Initialize an empty stack
    
    for bracket in brackets:
        # If the bracket is an opening bracket, push it onto the stack
        if bracket == "(":
            stack.append(bracket)
        # If the bracket is a closing bracket and the stack is empty, return False
        elif bracket == ")" and not stack:
            return False
        # If the bracket is a closing bracket and the stack is not empty, pop the opening bracket from the stack
        elif bracket == ")":
            stack.pop()
    
    # If the stack is empty after checking all brackets, return True
    # If the stack is not empty, return False because there are unmatched opening brackets
    return not stack

# Test the function
print(correct_bracketing("("))  # False
print(correct_bracketing("()"))  # True
print(correct_bracketing("(()())"))  # True
print(correct_bracketing(")(()"))  # False
```

This script uses a stack data structure to keep track of the opening brackets. It iterates over the input string, pushing opening brackets onto the stack and popping them off when it encounters a corresponding closing bracket. If it encounters a closing bracket without an opening bracket on the stack, it immediately returns False. At the end of the iteration, it checks if the stack is empty. If it is, that means every opening bracket had a corresponding closing bracket, so it returns True. If the stack is not empty, that means there were unmatched opening brackets, so it returns False.