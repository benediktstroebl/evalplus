```python
def correct_bracketing(brackets: str) -> bool:
    """
    Returns True if every opening bracket has a corresponding closing bracket.

    :param brackets: A string of "<" and ">".
    :return: True if every opening bracket has a corresponding closing bracket, False otherwise.
    """
    opening_count = 0  # Count of opening brackets
    for bracket in brackets:
        if bracket == "<":
            opening_count += 1  # If we see an opening bracket, increment the count
        elif bracket == ">":
            if opening_count == 0:  # If there are no opening brackets left, return False
                return False
            opening_count -= 1  # If we see a closing bracket, decrement the count
    return opening_count == 0  # If the count is zero after processing all brackets, return True


# Test cases
print(correct_bracketing("<"))  # False
print(correct_bracketing("<>"))  # True
print(correct_bracketing("<<><>>"))  # True
print(correct_bracketing("><<>"))  # False
```

This script uses a simple counter to keep track of the number of opening brackets encountered. When it sees a closing bracket, it decrements the counter. If the counter drops to zero, it means there are no opening brackets left, so it returns False. If the counter is zero after processing all brackets, it means every opening bracket has a corresponding closing bracket, so it returns True.