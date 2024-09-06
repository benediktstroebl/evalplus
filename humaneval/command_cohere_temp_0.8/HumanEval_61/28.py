```python
def correct_bracketing(brackets):
    open_brackets = len(brackets.split('('))
    close_brackets = len(brackets.split(')'))
    return open_brackets == close_brackets
```

This script defines a function `correct_bracketing` that takes a string `brackets` as input. It calculates the balance of opening and closing brackets by splitting the input string into three parts: `('(', ')', '(')`. It then measures the length of the middle part, which should be equal to the difference between opening and closing brackets if the brackets are balanced.

To safely split the string into three parts, the `split` method is used with the `(` and `)` characters as a separator. The method returns a tuple, and the length of this tuple corresponds to the number of occurrences of `(` and `)` in the string.

The example usage in the function's docstring demonstrates the expected behavior:
```python
>>> correct_brackets("(")
False
>>> correct_brackets("()")
True
>>> correct_brackets("(()())")
True
>>> correct_brackets(")(()")
False
```