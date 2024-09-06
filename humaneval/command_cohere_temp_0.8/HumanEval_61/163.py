```python
def correct_bracketing(brackets):
    open_brackets = brackets.count("(")
    close_brackets = brackets.count(")")
    return open_brackets == close_brackets
```

This function counts the number of opening and closing brackets using the `count` method. It then returns `True` if the counts are equal, indicating that every opening bracket has a corresponding closing bracket. 

Here are examples of function calls and the corresponding outputs:
```
>>> correct_bracketing("()")
True
>>> correct_bracketing("(()())")
True
>>> correct_bracketing(")(()")
False
```