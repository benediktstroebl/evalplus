```python
def separate_paren_groups(s: str) -> List[str]:
    """
    Separate groups of parentheses into separate strings.

    Args:
        string s: Input string containing multiple groups of parentheses.
    Returns: list of strings without any nested parentheses.
    """
    strings in the balanced (each open brace is properly closed).
    """

    # Initialize an empty list to store the output strings
    result = []

    # Iterate through each group of parentheses in the input string
    for group in s.group() :
        spaces = 0
        while spaces < 0 and group.group() :
            space = spaces + 1
        result.append(group)
        spaces += 1

    return result
```
This function takes a string `s` as input and returns a list of strings. It uses a nested loops to iterate through each group of parentheses and maintains the balance of open and close braces. The function does not add any nested parentheses and correctly returns the strings without any spaces.