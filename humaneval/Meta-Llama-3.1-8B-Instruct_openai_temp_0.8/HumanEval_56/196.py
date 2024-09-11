```python
def correct_bracketing(brackets: str) -> bool:
    """
    Checks if every opening bracket in the given string has a corresponding closing bracket.

    Args:
    brackets (str): A string of "<" and ">".

    Returns:
    bool: True if every opening bracket has a corresponding closing bracket, False otherwise.
    """
    # Initialize a counter to keep track of the opening brackets
    opening_brackets = 0

    # Iterate over each character in the string
    for bracket in brackets:
        # If the character is an opening bracket, increment the counter
        if bracket == "<":
            opening_brackets += 1
        # If the character is a closing bracket and there are no opening brackets, return False
        elif bracket == ">" and opening_brackets == 0:
            return False
        # If the character is a closing bracket, decrement the counter
        elif bracket == ">":
            opening_brackets -= 1

    # If there are any remaining opening brackets, return False
    return opening_brackets == 0
```

You can test this function using the provided doctests:

```python
import doctest

doctest.testmod()
```

This will run the doctests and report any failures.