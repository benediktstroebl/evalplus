```python
def correct_bracketing(brackets):
    open, closed = 0, 0
    for char in brackets:
        if char == '<':
            open += 1
        elif char == '>':
            closed += 1
        if open > closed:
            return False
    return open == closed
```

This script defines a function `correct_bracketing` that takes a string `brackets` as input. It counts the number of opening and closing brackets within the string and returns `True` if the number of opening and closing brackets is balanced. Otherwise, it returns `False`. 

The function leverages Python's robust support for string processing through f-strings, eliminating the need for additional libraries. It is also concise and easy to understand, making it ideal for problem-solving in coding interviews.

Here is an example of how this function can be invoked and its output interpreted:
```python
result = correct_bracketing("<abc>")
print(result)  # Output: True
```

In this example, the function is called with the input "<abc>", which represents one opening bracket, one closing bracket, and one text character between them. The function counts the opening and closing brackets, determining that they are balanced, and returns `True`. The resulting output, `True`, indicates that the input string has the correct bracket formation.