```python
def correct_bracketing(brackets: str) -> bool:
    """
    Checks if every opening bracket in the input string has a corresponding closing bracket.

    Args:
    brackets (str): A string containing only '(' and ')'.

    Returns:
    bool: True if every opening bracket has a corresponding closing bracket, False otherwise.
    """
    bracket_stack = []  # Initialize an empty stack

    for bracket in brackets:  # Iterate over each character in the input string
        if bracket == '(':  # If the character is an opening bracket
            bracket_stack.append(bracket)  # Push it onto the stack
        elif bracket == ')':  # If the character is a closing bracket
            if not bracket_stack:  # If the stack is empty (i.e., there's no matching opening bracket)
                return False  # Return False, as there's an unbalanced closing bracket
            bracket_stack.pop()  # Remove the matching opening bracket from the stack

    return not bracket_stack  # Return True if the stack is empty (i.e., all brackets were balanced), False otherwise


# Example use cases
print(correct_bracketing("("))  # False
print(correct_bracketing("()"))  # True
print(correct_bracketing("(()())"))  # True
print(correct_bracketing(")(()"))  # False
```

In this code:

*   We use a stack to keep track of the opening brackets we encounter as we iterate over the input string.
*   When we encounter a closing bracket, we check if the stack is empty (i.e., there's no matching opening bracket). If it is, we immediately return False.
*   If we successfully iterate over the entire string without returning False, we check if the stack is empty (i.e., all brackets were balanced). If it is, we return True; otherwise, we return False.