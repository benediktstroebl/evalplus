```python
def correct_bracketing(brackets: str) -> bool:
    """
    This function checks if a string of brackets has correct bracketing.
    
    Args:
    brackets (str): A string containing only "(" and ")".
    
    Returns:
    bool: True if every opening bracket has a corresponding closing bracket, False otherwise.
    """
    # Initialize a stack to store the opening brackets
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
    # If the stack is not empty, there were some opening brackets without corresponding closing brackets
    return not stack


# Test the function
if correct_bracketing("("):
    print("False")
if correct_bracketing("()"):
    print("True")
if correct_bracketing("(()())"):
    print("True")
if correct_bracketing(")(()"):
    print("False")
```

In this script, we use a stack data structure to keep track of the opening brackets. When we encounter a closing bracket, we check if the stack is empty. If it is, we return False because there's no corresponding opening bracket. If the stack is not empty, we pop the opening bracket from the stack. After iterating over the entire string, we check if the stack is empty. If it is, every opening bracket had a corresponding closing bracket, so we return True. If the stack is not empty, there were some opening brackets without corresponding closing brackets, so we return False.