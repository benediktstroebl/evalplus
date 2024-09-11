### Correct Bracketing
#### Problem Description
This script takes a string of "<" and ">" as input and returns `True` if every opening bracket has a corresponding closing bracket, and `False` otherwise.

#### Solution
```python
def correct_bracketing(brackets: str) -> bool:
    """
    brackets is a string of "<" and ">".
    return True if every opening bracket has a corresponding closing bracket.
    
    >>> correct_bracketing("<")
    False
    >>> correct_bracketing("<>")
    True
    >>> correct_bracketing("<<><>>")
    True
    >>> correct_bracketing("><<>")
    False
    """
    stack = []
    
    # Iterate over each character in the string
    for bracket in brackets:
        # If the character is an opening bracket, push it onto the stack
        if bracket == "<":
            stack.append(bracket)
        # If the character is a closing bracket, check if the stack is empty
        elif bracket == ">":
            # If the stack is empty, return False because there's no corresponding opening bracket
            if not stack:
                return False
            # If the stack is not empty, pop the opening bracket from the stack
            else:
                stack.pop()
    
    # After iterating over the entire string, return True if the stack is empty, and False otherwise
    return not stack

# Example usage:
print(correct_bracketing("<"))  # False
print(correct_bracketing("<>"))  # True
print(correct_bracketing("<<><>>"))  # True
print(correct_bracketing("><<>"))  # False
```
This script uses a stack data structure to keep track of the opening brackets encountered so far. When a closing bracket is encountered, it checks if the stack is empty. If it is, it means there's no corresponding opening bracket, so it returns False. Otherwise, it pops the opening bracket from the stack. After iterating over the entire string, it checks if the stack is empty. If it is, it means all opening brackets have been matched with corresponding closing brackets, so it returns True. Otherwise, it returns False.