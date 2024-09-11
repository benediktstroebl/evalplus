```python
def correct_bracketing(brackets: str):
    """
    Checks if every opening bracket in the string has a corresponding closing bracket.

    Args:
        brackets (str): A string consisting of "(" and ")".

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
        # If the character is a closing bracket and the stack is empty, return False
        elif bracket == ")" and not stack:
            return False
        # If the character is a closing bracket and the stack is not empty, pop the opening bracket from the stack
        elif bracket == ")" and stack:
            stack.pop()

    # After iterating over the entire string, if the stack is empty, return True
    # If the stack is not empty, it means there are unmatched opening brackets, so return False
    return not stack


# Test cases
if __name__ == "__main__":
    print(correct_bracketing("("))  # False
    print(correct_bracketing("()"))  # True
    print(correct_bracketing("(()())"))  # True
    print(correct_bracketing(")(()"))  # False
```

This script defines a function `correct_bracketing` that checks if every opening bracket in the string has a corresponding closing bracket. It uses a stack to keep track of the opening brackets and returns True if every opening bracket has a corresponding closing bracket, and False otherwise. The script also includes test cases to verify the correctness of the function.