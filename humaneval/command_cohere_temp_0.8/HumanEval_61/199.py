```python
def correct_bracketing(brackets):
    open_brackets = brackets.count("(")
    close_brackets = brackets.count(")")
    return open_brackets == close_brackets
```

This function uses the `count` method to calculate the number of opening and closing brackets. It then returns True if the counts are equal, implying that every opening bracket has a corresponding closing bracket. The provided tests correctly illustrate the scenarios of correctly and incorrectly balanced brackets. 

```python
# Tests
test_cases = [
    ("(", "False"),
    ("()", "True"),
    ("(()())", "True"),
    (")(()", "False")
]

for brackets, expected in test_cases:
    assert correct_bracketing(brackets) == expected
```