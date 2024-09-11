```python
def correct_bracketing(brackets: str) -> bool:
    """
    This function checks if every opening bracket in a string has a corresponding closing bracket.

    Args:
    brackets (str): A string containing only "(" and ")".

    Returns:
    bool: True if every opening bracket has a corresponding closing bracket, False otherwise.
    """

    # Initialize a counter for the brackets
    counter = 0

    # Iterate over each character in the string
    for bracket in brackets:
        # If the character is an opening bracket, increment the counter
        if bracket == "(":
            counter += 1
        # If the character is a closing bracket and the counter is greater than 0, decrement the counter
        elif bracket == ")" and counter > 0:
            counter -= 1

    # If the counter is zero, all brackets were matched correctly
    return counter == 0


# Test the function
print(correct_bracketing("("))  # False
print(correct_bracketing("()"))  # True
print(correct_bracketing("(()())"))  # True
print(correct_bracketing(")(()"))  # False
```

However, we can also use the `count()` method and the fact that strings in Python are iterable to do this in one line:

```python
def correct_bracketing(brackets: str) -> bool:
    """
    This function checks if every opening bracket in a string has a corresponding closing bracket.

    Args:
    brackets (str): A string containing only "(" and ")".

    Returns:
    bool: True if every opening bracket has a corresponding closing bracket, False otherwise.
    """
    return brackets.count("(") == brackets.count(")")

# Test the function
print(correct_bracketing("("))  # False
print(correct_bracketing("()"))  # True
print(correct_bracketing("(()())"))  # True
print(correct_bracketing(")(()"))  # False
```

This function works by comparing the number of opening brackets ( "(" ) to the number of closing brackets ( ")" ). If they are equal, it means that every opening bracket has a corresponding closing bracket, and the function returns True. Otherwise, it returns False.