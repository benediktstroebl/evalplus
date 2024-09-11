```python
def correct_bracketing(brackets: str):
    """
    brackets is a string of "<" and ">".
    return True if every opening bracket has a corresponding closing bracket.

    :param brackets: A string containing only "<" and ">"
    :return: True if every opening bracket has a corresponding closing bracket, False otherwise
    """
    # Initialize a counter to track the number of open brackets
    open_brackets = 0

    # Iterate over each character in the string
    for bracket in brackets:
        # If the character is an open bracket, increment the counter
        if bracket == "<":
            open_brackets += 1
        # If the character is a close bracket and there are open brackets, decrement the counter
        elif bracket == ">" and open_brackets > 0:
            open_brackets -= 1
        # If the character is a close bracket and there are no open brackets, return False
        elif bracket == ">":
            return False

    # If there are still open brackets after iterating over the entire string, return False
    if open_brackets > 0:
        return False

    # If the function hasn't returned False, return True
    return True

# Test cases
print(correct_bracketing("<"))  # False
print(correct_bracketing("<>"))  # True
print(correct_bracketing("<<><>>"))  # True
print(correct_bracketing("><<>"))  # False
```

This script uses a simple counter to track the number of open brackets in the string. When an open bracket is encountered, the counter is incremented, and when a closing bracket is encountered, the counter is decremented. If the string ends with a closing bracket when there are open brackets remaining, the function returns False. Otherwise, the function returns True if the counter reaches zero at the end of the string.