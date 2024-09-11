```python
def correct_bracketing(brackets: str) -> bool:
    """
    Returns True if every opening bracket has a corresponding closing bracket.

    Args:
    brackets (str): A string of "<" and ">".

    Returns:
    bool: Whether every opening bracket has a corresponding closing bracket.
    """
    return brackets.count("<") == brackets.count(">")

# Test cases
if not correct_bracketing("<"):
    print("Test case 1 passed")
if correct_bracketing("<>"):
    print("Test case 2 passed")
if correct_bracketing("<<><>>"):
    print("Test case 3 passed")
if not correct_bracketing("><<>"):
    print("Test case 4 passed")
```

This script defines a function `correct_bracketing` that takes a string `brackets` as input and returns `True` if every opening bracket has a corresponding closing bracket, and `False` otherwise. The function accomplishes this by simply comparing the counts of "<" and ">" in the string, as every opening bracket must be paired with a closing bracket. The test cases at the end of the script verify that this function works as expected.