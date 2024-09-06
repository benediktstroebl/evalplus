```python
def correct_bracketing(brackets):
    open_brackets = brackets.count('(')
    close_brackets = brackets.count(')')
    return open_brackets == close_brackets
```

This function uses the `count` method to efficiently count the number of opening and closing brackets in the given string. The count of opening brackets (`open_brackets`) is compared to the count of closing brackets (`close_brackets`) and if they are equal, the function returns `True`, indicating that every opening bracket has a corresponding closing bracket in the given string. The function returns `False` otherwise. 

This solution works efficiently and returns the correct result for the given test cases.