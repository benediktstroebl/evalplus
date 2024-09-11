```python
def correct_bracketing(brackets: str):
    """
    Check if every opening bracket in a string has a corresponding closing bracket.

    Args:
    brackets (str): A string consisting of "(" and ")".

    Returns:
    bool: True if every opening bracket has a corresponding closing bracket, False otherwise.
    """
    stack = []  # Initialize an empty stack to keep track of opening brackets

    for bracket in brackets:
        # If the bracket is an opening bracket, push it onto the stack
        if bracket == "(":
            stack.append(bracket)
        # If the bracket is a closing bracket, check if the stack is empty
        elif bracket == ")":
            # If the stack is empty, there's no corresponding opening bracket, so return False
            if not stack:
                return False
            # If the stack is not empty, pop the opening bracket from the stack
            else:
                stack.pop()

    # After checking all brackets, return True if the stack is empty (no unpaired opening brackets)
    # and False if the stack is not empty (unpaired opening brackets)
    return not stack

if __name__ == "__main__":
    print(correct_bracketing("("))  # False
    print(correct_bracketing("()"))  # True
    print(correct_bracketing("(()())"))  # True
    print(correct_bracketing(")(()"))  # False
```

This script solves the problem by using a stack data structure. It iterates through each bracket in the string, pushing opening brackets onto the stack and popping them off when it encounters a closing bracket. If it encounters a closing bracket without an opening bracket on the stack, it immediately returns False. After checking all brackets, it returns True if the stack is empty (no unpaired opening brackets) and False otherwise.