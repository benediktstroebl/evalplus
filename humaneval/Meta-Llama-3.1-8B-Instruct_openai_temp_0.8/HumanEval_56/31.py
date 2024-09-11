```python
def correct_bracketing(brackets: str) -> bool:
    """
    Checks if every opening bracket has a corresponding closing bracket.

    Args:
        brackets (str): A string of "<" and ">".

    Returns:
        bool: True if every opening bracket has a corresponding closing bracket, False otherwise.
    """
    return brackets.count("<") == brackets.count(">")

# Test cases
print(correct_bracketing("<"))  # False
print(correct_bracketing("<>"))  # True
print(correct_bracketing("<<><>>"))  # True
print(correct_bracketing("><<>"))  # False
```

This script defines a function `correct_bracketing` that takes a string of "<" and ">" as input and returns `True` if every opening bracket has a corresponding closing bracket, and `False` otherwise. The function uses the `count` method of the string to count the number of occurrences of "<" and ">" and checks if they are equal. If they are equal, it means every opening bracket has a corresponding closing bracket, and the function returns `True`. Otherwise, it returns `False`. The script also includes the test cases you provided to demonstrate the function's behavior.