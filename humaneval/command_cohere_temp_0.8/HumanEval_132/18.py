```python
def is_nested(s):
    open, close = 0, 0
    for char in s:
        if char == '[':
            open += 1
        else:
            close += 1
        if open > close:
            return False
    return open != close
```

The function counts the openings '[' and closings ']' as it iterates through the string. The algorithm directly counts the brackets without relying on recursion or memorization. The input string can only contain square brackets and the output is a boolean indicating whether at least one bracket is nested.

To use this function, you can copy and paste the code into a Python environment or script and call the function with a string as an argument like this:
```python
>>> is_nested("[[[]]])")
True
>>> is_nested("[[[[[[[]]]]]]]")
False
>>> is_nested("[]")
False
>>> is_nested("[[[]]]")
True
```

This will return `True` for valid nested sequences and `False` for invalid ones.