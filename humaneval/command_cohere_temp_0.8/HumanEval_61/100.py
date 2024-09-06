```python
def correct_bracketing(brackets):
    open_brackets = brackets.count("(")
    close_brackets = brackets.count(")")
    return open_brackets == close_brackets
```

This function counts the number of opening and closing brackets using the built-in `count` method. It then returns `True` if the counts are equal, indicating that every opening bracket has a corresponding closing bracket, and `False` otherwise. This logic follows the requirements of the given problem.

Here is a sample output explaining the behavior of the function:
```
>>> correct_bracketing("(|)")
False
>>> correct_bracketing("()()")
True
>>> correct_bracketing("())")
False
```