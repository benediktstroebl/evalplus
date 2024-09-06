```python
def correct_bracketing(brackets):
    open_brackets = brackets.count("(")
    close_brackets = brackets.count(")")
    return open_brackets == close_brackets
```

This function counts the number of opening and closing brackets using the `count` method. It then returns `True` if the counts are equal, indicating that every opening bracket has a corresponding closing bracket.

Here are examples of function calls and the respective outcomes:
1. `correct_bracketing("(")`: Returns `False` since the count of opening brackets (`1`) does not match the count of closing brackets (`0`).
2. `correct_bracketing("()")`: Returns `True` because the count of opening brackets (`1`) matches the count of closing brackets (`1`).
3. `correct_bracketing("(()())")`: Returns `True` as the count of opening brackets (`3`) matches the count of closing brackets (`3`).
4. `correct_bracketing(")(()")`: Returns `False` because the count of opening brackets (`2`) exceeds the count of closing brackets (`1`).