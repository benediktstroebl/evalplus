```markdown
### Correct Bracketing Function

This script provides a function `correct_bracketing` that checks if every opening bracket in a string has a corresponding closing bracket.

#### Code

```python
def correct_bracketing(brackets: str) -> bool:
    """
    Check if every opening bracket in a string has a corresponding closing bracket.

    Args:
    brackets (str): A string of "(" and ")".

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
        # If the character is a closing bracket, decrement the counter
        elif bracket == ")":
            # If the counter is already 0, it means there's no corresponding opening bracket
            if counter == 0:
                return False
            # Decrement the counter
            counter -= 1
    # If the counter is not 0 after iterating over the string, it means there are some opening brackets without corresponding closing brackets
    return counter == 0
```

#### Example Use Cases

```python
print(correct_bracketing("("))  # False
print(correct_bracketing("()"))  # True
print(correct_bracketing("(()())"))  # True
print(correct_bracketing(")(()"))  # False
```
```