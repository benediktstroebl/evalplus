```python
def correct_bracketing(brackets):
    open_brackets = brackets.count('(')
    close_brackets = brackets.count(')')
    return open_brackets == close_brackets
```

This function uses the `count` method to efficiently count the number of opening and closing brackets in the given string. It then returns `True` if these counts are equal, implying that every opening bracket has a corresponding closing bracket, and `False` otherwise. This solution has a time complexity of `O(n)` since it requires iterating the input string twice to count the brackets, regardless of the input size.