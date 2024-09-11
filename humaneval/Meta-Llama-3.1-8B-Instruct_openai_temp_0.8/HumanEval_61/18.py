```python
def correct_bracketing(brackets: str) -> bool:
    """
    Checks if a string of parentheses has correct bracketing.

    Args:
    brackets (str): A string of "(" and ")".

    Returns:
    bool: True if every opening bracket has a corresponding closing bracket, False otherwise.
    """
    # Initialize a stack to keep track of opening brackets
    stack = []
    
    # Iterate over each character in the string
    for bracket in brackets:
        # If the character is an opening bracket, push it onto the stack
        if bracket == "(":
            stack.append(bracket)
        # If the character is a closing bracket, check if the stack is empty
        elif bracket == ")":
            # If the stack is empty, return False because there's no corresponding opening bracket
            if not stack:
                return False
            # If the stack is not empty, pop the opening bracket from the stack
            else:
                stack.pop()
    
    # After iterating over the entire string, return True if the stack is empty and False otherwise
    return not stack

# Test cases
print(correct_bracketing("("))  # False
print(correct_bracketing("()"))  # True
print(correct_bracketing("(()())"))  # True
print(correct_bracketing(")(("))  # False
```

In this script, we use a stack data structure to keep track of the opening brackets. When we encounter an opening bracket, we push it onto the stack. When we encounter a closing bracket, we check if the stack is empty. If it is, we return False because there's no corresponding opening bracket. If the stack is not empty, we pop the opening bracket from the stack. After iterating over the entire string, we return True if the stack is empty (meaning every opening bracket has a corresponding closing bracket) and False otherwise.