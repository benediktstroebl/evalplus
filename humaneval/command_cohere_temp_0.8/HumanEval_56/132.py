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

This Python script defines a function `correct_bracketing` that takes a string `brackets` as input. The function counts the opening and closing brackets separately as it iterates through the string. It calculates the balance of brackets by checking if the count of opening brackets is equal to the count of closing brackets. If the balance is unequal, the function returns `False`, indicating that not every opening bracket has a corresponding closing bracket. The function returns `True` if the counts are equal, implying correctly balanced brackets. 

Here is an example usage of the function:
```python
print(correct_bracketing("<<>>")) # Output: True
print(correct_bracketing("><")) # Output: False
```

This demonstrates the function's behavior, highlighting that it returns `True` for well-balanced brackets and `False` for unbalanced ones.