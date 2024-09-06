```python
def correct_bracketing(brackets):
    open_brackets = brackets.count('(')
    close_brackets = brackets.count(')')
    return open_brackets == close_brackets
```

This function uses the `count` method to check for the occurrence of both opening and closing brackets and then compares their counts using the `==` operator. The function returns `True` if the counts are equal, indicating that every opening bracket has a corresponding closing bracket, and `False` otherwise.