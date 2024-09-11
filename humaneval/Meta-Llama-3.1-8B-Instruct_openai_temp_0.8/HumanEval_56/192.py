```python
def correct_bracketing(brackets: str):
    """
    Checks if every opening bracket has a corresponding closing bracket.

    Args:
    brackets (str): A string of "<" and ">".

    Returns:
    bool: True if every opening bracket has a corresponding closing bracket, False otherwise.
    """
    
    # Initialize a counter to keep track of opening and closing brackets
    counter = 0
    
    # Iterate over each character in the string
    for bracket in brackets:
        # If the bracket is an opening bracket, increment the counter
        if bracket == "<":
            counter += 1
        # If the bracket is a closing bracket, decrement the counter
        elif bracket == ">":
            counter -= 1
        # If the counter becomes negative, it means there's a closing bracket without an opening one
        if counter < 0:
            return False
    
    # If the counter isn't zero after iterating over the entire string, it means there are opening brackets without closing ones
    return counter == 0


# Test cases
print(correct_bracketing("<"))    # False
print(correct_bracketing("<>"))   # True
print(correct_bracketing("<<><>>"))  # True
print(correct_bracketing("><<>"))   # False
```