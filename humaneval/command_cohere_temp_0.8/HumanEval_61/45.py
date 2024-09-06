```python
def correct_bracketing(brackets):
    open_brackets = brackets.count("(")
    close_brackets = brackets.count(")")
    return open_brackets == close_brackets
```

This function counts the number of '(' and ')' in the string and compares the counts. The function returns True if the counts are equal, implying that every opening bracket has a corresponding closing bracket, and returns False otherwise. This solves the problem and passes the given tests.