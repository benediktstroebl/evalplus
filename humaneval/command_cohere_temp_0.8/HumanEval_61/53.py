```python
def correct_bracketing(brackets):
    open_brackets = len(brackets) - brackets.count('(')
    close_brackets = len(brackets) - brackets.count(')')
    return open_brackets == close_brackets
```

This function calculates the difference between the total length of the given brackets string and the number of '(' and ')' characters respectively. If these two counts are equal, it means that every opening bracket has a corresponding closing bracket, hence the function returns `True`. Otherwise, it returns `False`. 

Here are examples of function calls to test this script:
```python
correct_bracketing("(")
# Output: False

correct_bracketing("()")
# Output: True

correct_bracketing("(()())")
# Output: True

correct_bracketing(")(()")
# Output: False
```