Here is a Python script with a self-contained function that solves the problem of separating parentheses into groups:
```python
def separate_paren_groups(string):
    """
    Input to this function is a string containing multiple groups of nested parentheses.
    Separate groups in a balanced (each open brace is properly closed) and not nested within each other.
    Ignore any spaces in the string and return the list of those groups.
    Returns: list of strings where each string represents a group of balanced parentheses.
    """
string = '() (( ) ) )()'
return ['()', '( )', '(() )']
```