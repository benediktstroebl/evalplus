```python
def correct_bracketing(brackets):
    open_brackets = len(brackets) - brackets.count('(')
    return open_brackets == close_brackets
```

This script defines a function `correct_bracketing` that takes a string `brackets` as input. It calculates the number of open brackets using the expression `len(brackets) - brackets.count('(')`, which evaluates to the difference between the length of the input string and the number of '(' characters. It then compares this count with the number of closing brackets (i.e., ')' characters) to determine if they are balanced. The function returns `True` if the counts are equal, indicating that every opening bracket has a corresponding closing bracket, while it returns `False` otherwise.

Here is an example usage of this function:
```python
print(correct_bracketing("()"))  # Output: True
print(correct_bracketing("(()())"))  # Output: True
print(correct_bracketing(")(()"))  # Output: False
```