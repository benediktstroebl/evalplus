```python
def correct_bracketing(brackets):
    open_brackets = len(brackets) - brackets.count('(')
    return open_brackets == close_brackets
```

This function directly calculates the difference between the length of the given brackets string and the number of '(' (open brackets) to determine the number of ')' (close brackets) needed. It then returns whether the two values are equal, denoting whether all opening brackets have a corresponding closing bracket. 

Here is a snippet of tests to ensure the function works properly:
```python
>>> correct_bracketing("(()())")
True
>>> correct_bracketing(")(())")
False
>>> correct_bracketing("abc")
False
>>> correct_bracketing("(]")
False
>>> correct_bracketing("())")
False
>>> correct_bracketing("($10")
False
```