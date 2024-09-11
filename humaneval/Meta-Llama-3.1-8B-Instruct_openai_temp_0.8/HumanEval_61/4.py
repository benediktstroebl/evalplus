```python
def correct_bracketing(brackets: str) -> bool:
    """
    Checks if every opening bracket in the string has a corresponding closing bracket.

    Args:
    brackets (str): A string of "(" and ")".

    Returns:
    bool: True if every opening bracket has a corresponding closing bracket, False otherwise.
    """
    stack = []  # Initialize an empty stack to store opening brackets

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

    # After iterating over the entire string, if the stack is empty, return True
    # This means every opening bracket has a corresponding closing bracket
    return not stack


# Test cases
if __name__ == "__main__":
    print(correct_bracketing("("))  # False
    print(correct_bracketing("()"))  # True
    print(correct_bracketing("(()())"))  # True
    print(correct_bracketing(")(()"))  # False
```

This script defines a function `correct_bracketing` that takes a string of brackets as input and returns a boolean indicating whether every opening bracket has a corresponding closing bracket. It uses a stack to keep track of opening brackets and checks for corresponding closing brackets by popping them from the stack. If the stack is empty at the end, it means every opening bracket has a corresponding closing bracket.