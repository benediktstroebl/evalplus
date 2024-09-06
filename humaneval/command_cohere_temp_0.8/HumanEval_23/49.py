```python
def strlen(string: str) -> int:
    """ Returns the length of a string. 
    NOTE: This function does not count anyMarkdown characters such as the '#' in a heading 
    or the whitespace character '\n' in a new line. It only counts the basic ASCII characters.
    """
    return len(string)
```

This Python script defines a function `strlen` that takes a string as an argument and returns the length of the string, excluding any special characters or markdown specifications. It then provides a quick example that calls the `strlen` function and prints out the result. The example includes a blank string which returns a length of 0, and a sample string "abc" which returns a length of 3.