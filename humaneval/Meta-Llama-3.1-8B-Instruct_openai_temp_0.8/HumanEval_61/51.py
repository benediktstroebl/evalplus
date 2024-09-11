```python
def correct_bracketing(brackets: str) -> bool:
    """
    Checks if every opening bracket in the string has a corresponding closing bracket.

    Args:
    brackets (str): A string consisting of "(" and ")".

    Returns:
    bool: True if every opening bracket has a corresponding closing bracket, False otherwise.
    """
    stack = []  # Initialize an empty stack to store the opening brackets
    for bracket in brackets:  # Iterate over each character in the string
        if bracket == "(":  # If the character is an opening bracket
            stack.append(bracket)  # Push it onto the stack
        elif bracket == ")":  # If the character is a closing bracket
            if not stack:  # If the stack is empty (i.e., there's no matching opening bracket)
                return False  # Return False
            stack.pop()  # Otherwise, pop the matching opening bracket from the stack
    return not stack  # If the stack is empty after iterating over the entire string, return True; otherwise, return False


# Test cases
if __name__ == "__main__":
    print(correct_bracketing("("))  # False
    print(correct_bracketing("()"))  # True
    print(correct_bracketing("(()())"))  # True
    print(correct_bracketing(")(()"))  # False
```