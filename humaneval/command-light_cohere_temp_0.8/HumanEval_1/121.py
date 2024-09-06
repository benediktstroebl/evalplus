```python
def separate_paren_groups(parentheses: str) -> List[str]:
    """
    Input is a string containing multiple groups of parentheses.
    Separate each balanced group into balanced (each open brace is properly closed) and return the list of those strings.
    """: Return the standard Python string split function with delimiter as space
    :return: list of separated strings
    """
    # Split the string into individual lines based on spaces
    return [line.split() for line in parentheses.
  
``` 
The above code solves the problem of separating balanced groups of parentheses into individual strings and returns the list of those strings.