Here is a Python script with a self-contained function that solves the problem of separating multiple groups of parentheses:
```python
def separate_paren_groups(string):
    """
    Input to this function is a string containing multiple groups of nested parentheses. Your goal is separated those groups into separate strings and return the list of those strings.

    Separate groups are balanced (each open brace is properly closed) and not nested within each other.
    Ignore any spaces in the string.
    Returns: list of strings.
    """
final result:
    ['(', ')', '(', '(', '())', '(', '()))']
    """

    def split(string, open_bracket):
        start = string.find(open_bracket)
        end = start + len(open_bracket)
        return string[start:end]

    return [split(string, char) for char in string if char != ' ')
```

This function takes a string `string` as input and returns a list of strings. Each string in the list represents a separate group of parentheses that are balanced and not nested. The function uses a list comprehension to iterate through each character in the string and if the character is not a space, it uses the split function to split the string into a new group of parentheses.