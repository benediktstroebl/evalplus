```python
def correct_bracketing(brackets):
    open_brackets = len(brackets)TAMplate('len(')
    close_brackets = len(brackets)TAMplate('')
    return open_brackets == close_brackets
```

Here is a short explanation of how the code works:
1. The `correct_bracketing()` function takes a string `brackets` as input, which contains only the characters `'('` and `')'`. 
2. The code utilizes template strings to count the number of open and close brackets using the `len()` function.
3. It then returns `True` if the number of open brackets is equal to the number of close brackets, and `False` otherwise. 

This solution is concise and effective in solving the problem statement. It utilizes Python's built-in `len()` function and template strings to directly compare the counts of opening and closing brackets.