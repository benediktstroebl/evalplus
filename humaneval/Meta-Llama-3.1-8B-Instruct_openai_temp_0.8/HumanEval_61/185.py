```python
def correct_bracketing(brackets: str):
    """
    brackets is a string of "(" and ")".
    return True if every opening bracket has a corresponding closing bracket.

    :param brackets: A string of "(" and ")"
    :return: True if every opening bracket has a corresponding closing bracket, False otherwise
    """
    stack = []  # Initialize an empty stack

    for bracket in brackets:
        # If the bracket is an opening bracket, push it to the stack
        if bracket == "(":
            stack.append(bracket)
        # If the bracket is a closing bracket and the stack is empty, return False
        elif bracket == ")" and not stack:
            return False
        # If the bracket is a closing bracket and the stack is not empty, pop the opening bracket from the stack
        elif bracket == ")":
            stack.pop()

    # After iterating over the string, return True if the stack is empty and False otherwise
    return not stack


# Test cases
print(correct_bracketing("("))  # False
print(correct_bracketing("()"))  # True
print(correct_bracketing("(()())"))  # True
print(correct_bracketing(")(()"))  # False
```

This script uses a stack data structure to keep track of the opening brackets. It iterates over the string, pushing opening brackets onto the stack and popping them when it encounters corresponding closing brackets. If it encounters a closing bracket when the stack is empty, it immediately returns False. Finally, it checks if the stack is empty after iterating over the string, returning True if it is (i.e., every opening bracket had a corresponding closing bracket) and False otherwise.