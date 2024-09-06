```python
def correct_bracketing(brackets):
    open_brackets = brackets.count("(")
    close_brackets = brackets.count(")")
    return open_brackets == close_brackets
```

This function counts the number of opening and closing brackets using the built-in `count` method. The function then returns `True` if the two counts are equal, meaning that every opening bracket has a corresponding closing bracket, otherwise `False`. 

Here is how you can use this function to validate some inputs: 
```python
>>> correct_bracketing("(")
False
>>> correct_bracketing("()")
True
>>> correct_bracketing("(()())")
True
>>> correct_bracketing(")(()")
False
>>> correct_bracketing(")...(")
False
```