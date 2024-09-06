```python
def correct_bracketing(brackets):
    open_brackets = brackets.count('(')
    close_brackets = brackets.count(')')
    return open_brackets == close_brackets
```

This function counts the number of opening and closing brackets using the built-in `count` method. It then returns `True` if the counts are equal, indicating that every opening bracket has a corresponding closing bracket.

Here is a snippet of test code to test the functionality of the function:
```python
test_cases = [
    ("()", True),
    ("(())", True),
    ("()()", True),
    ("( )", False),
    ("( )(", False),
    ("(a)", False),
    ("(a)", "(:", False),
]

for brackets, result in test_cases:
    assert correct_bracketing(brackets) == result
```