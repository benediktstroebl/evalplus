```python
def correct_bracketing(brackets: str) -> bool:
    """
    Checks if every opening bracket in the given string has a corresponding closing bracket.

    Args:
    brackets (str): A string of "(" and ")".

    Returns:
    bool: True if every opening bracket has a corresponding closing bracket, False otherwise.

    >>> correct_bracketing("(")
    False
    >>> correct_bracketing("()")
    True
    >>> correct_bracketing("(()())")
    True
    >>> correct_bracketing(")(()")
    False
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
            # If the stack is not empty, pop the corresponding opening bracket from the stack
            else:
                stack.pop()
    
    # After iterating over the entire string, if the stack is empty, every opening bracket has a corresponding closing bracket, so return True
    # If the stack is not empty, there are unmatched opening brackets, so return False
    return not stack


# Test cases
print(correct_bracketing("("))  # False
print(correct_bracketing("()"))  # True
print(correct_bracketing("(()())"))  # True
print(correct_bracketing(")(()"))  # False
```