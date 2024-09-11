```python
def correct_bracketing(brackets: str):
    """
    Returns True if every opening bracket has a corresponding closing bracket.

    :param brackets: A string of "<" and ">"
    :return: True if brackets are correctly paired, False otherwise
    """
    stack = []
    for bracket in brackets:
        # If we encounter an opening bracket, push it onto the stack
        if bracket == "<":
            stack.append(bracket)
        # If we encounter a closing bracket, check if the stack is empty
        elif bracket == ">":
            # If the stack is empty, it means there's no corresponding opening bracket
            if not stack:
                return False
            # If the stack is not empty, pop the opening bracket
            else:
                stack.pop()
    # After checking all brackets, if the stack is empty, it means every opening bracket has a corresponding closing bracket
    return not stack


# Test cases
print(correct_bracketing("<"))  # False
print(correct_bracketing("<>"))  # True
print(correct_bracketing("<<><>>"))  # True
print(correct_bracketing("><<>"))  # False
```

This script uses a stack data structure to keep track of the opening brackets. When an opening bracket is encountered, it's pushed onto the stack. When a closing bracket is encountered, the stack is checked to see if it's empty. If it's empty, it means there's no corresponding opening bracket, so the function returns False. If the stack is not empty, the opening bracket is popped from the stack. After checking all brackets, if the stack is empty, it means every opening bracket has a corresponding closing bracket, so the function returns True.