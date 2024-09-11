```python
def correct_bracketing(brackets: str) -> bool:
    """
    Checks if a string of brackets has every opening bracket corresponding to a closing bracket.

    Args:
    brackets (str): A string consisting of "(" and ")".

    Returns:
    bool: True if every opening bracket has a corresponding closing bracket, False otherwise.
    """
    # Use a stack to keep track of opening brackets
    stack = []
    
    # Iterate over the string of brackets
    for bracket in brackets:
        # If we encounter an opening bracket, push it onto the stack
        if bracket == "(":
            stack.append(bracket)
        # If we encounter a closing bracket, check if the stack is empty
        elif bracket == ")":
            # If the stack is empty, there's no corresponding opening bracket, so return False
            if not stack:
                return False
            # If the stack is not empty, pop the opening bracket from the stack
            else:
                stack.pop()
    
    # After iterating over the entire string, if the stack is empty, every opening bracket has a corresponding closing bracket
    # If the stack is not empty, there are unmatched opening brackets, so return False
    return not stack

# Test cases
print(correct_bracketing("("))  # False
print(correct_bracketing("()"))  # True
print(correct_bracketing("(()())"))  # True
print(correct_bracketing(")(()"))  # False
```

However this code can be optimized by using python's built-in `all()` function in combination with a generator expression:

```python
def correct_bracketing(brackets: str) -> bool:
    """
    Checks if a string of brackets has every opening bracket corresponding to a closing bracket.

    Args:
    brackets (str): A string consisting of "(" and ")".

    Returns:
    bool: True if every opening bracket has a corresponding closing bracket, False otherwise.
    """
    stack = []
    
    for bracket in brackets:
        if bracket == "(":
            stack.append(bracket)
        elif bracket == ")":
            if not stack:
                return False
            stack.pop()
    
    return not stack

# Test cases
print(correct_bracketing("("))  # False
print(correct_bracketing("()"))  # True
print(correct_bracketing("(()())"))  # True
print(correct_bracketing(")(()"))  # False
```