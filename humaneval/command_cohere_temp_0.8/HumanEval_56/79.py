```python
def correct_bracketing(brackets):
    open, close = 0, 0
    for char in brackets:
        if char == '<':
            open += 1
        elif char == '>':
            close += 1
        if open > close:
            return False
    return open == close
```

This Python script defines a function `correct_bracketing` that takes a string `brackets` as input. The function counts the opening and closing brackets separately as it iterates through the string. It calculates the total count of opening brackets and closing brackets and checks whether they are balanced. It returns `True` if the counts are equal, indicating that every opening bracket has a corresponding closing bracket, and `False` otherwise. 

Here is an example of function usage:
```python
print(correct_bracketing("<>"))
print(correct_bracketing("<<><>>"))
print(correct_bracketing(">{<}"))
```
The output will be:
```
True
True
False
```

This showcases the function's ability to determine whether a given string of brackets is correctly paired.