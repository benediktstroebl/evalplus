```python
def correct_bracketing(brackets: str):
    """
    Checks if every opening bracket in a string has a corresponding closing bracket.

    Args:
        brackets (str): A string containing only "(" and ")".

    Returns:
        bool: True if every opening bracket has a closing bracket, False otherwise.
    """
    stack = []
    
    # Iterate over each character in the string
    for bracket in brackets:
        # If the character is an opening bracket, push it onto the stack
        if bracket == "(":
            stack.append(bracket)
        # If the character is a closing bracket, check if the stack is empty
        elif bracket == ")":
            # If the stack is empty, there's no corresponding opening bracket, so return False
            if not stack:
                return False
            # If the stack is not empty, pop the opening bracket from the stack
            else:
                stack.pop()
    
    # After iterating over the entire string, if the stack is empty, every opening bracket had a corresponding closing bracket
    return not stack

# Test cases
print(correct_bracketing("("))  # False
print(correct_bracketing("()"))  # True
print(correct_bracketing("(()())"))  # True
print(correct_bracketing(")(()"))  # False
```

In this script, we use a stack to keep track of the opening brackets. When we encounter an opening bracket, we push it onto the stack. When we encounter a closing bracket, we check if the stack is empty. If it is, there's no corresponding opening bracket, so we return False. If the stack is not empty, we pop the opening bracket from the stack. After iterating over the entire string, if the stack is empty, every opening bracket had a corresponding closing bracket, so we return True.