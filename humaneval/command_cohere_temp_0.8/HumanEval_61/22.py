```python
def correct_bracketing(brackets):
    open_brackets = brackets.count("(")
    close_brackets = brackets.count(")")
    return open_brackets == close_brackets
```

This function uses the `count` method to efficiently count the number of opening and closing brackets in the given string. The function returns `True` if the counts are equal, indicating that every opening bracket has a corresponding closing bracket, and `False` otherwise. 

Here is a simpler solution:
```python
def correct_bracketing(brackets):
    open_brackets = brackets.replace(")", "")
    return len(open_brackets) == 0
```

Which also returns True if every opening bracket has a closing one, or in other words if the resulting string after splitting by ')') is empty, implying that there is no leftover open brackets.