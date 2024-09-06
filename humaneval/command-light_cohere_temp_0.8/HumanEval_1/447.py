Here's the solution for the function `separate_paren_groups`:
```python
def separate_paren_groups(parentheses: str) -> List[str]:
    """
    Separate the groups of parentheses into separate strings.
    Return a balanced (each open brace is properly closed) and not nested within each other
    other.
    """
    list comprehension is easy to read, I made a little thing that makes the code more readable:
    """
    return [group.replace(r for r in ''.split(')')) for group in  parentheses.split('()') 
```

The `split()` function in Python is used to split a string into a list of substrings.  The `group()` function splits the entire string into a list of substrings based on whitespace.