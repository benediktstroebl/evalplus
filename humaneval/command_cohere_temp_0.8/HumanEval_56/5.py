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

The following test cases are submitted for this script:
```python
test_cases = [
    ('', False),
    ('<', False),
    ('>', False),
    ('<>', True),
    ('<<>>', True),
    ('<>', False),
    ('<<<>', True),
    ('<<>>', True),
    ('<<><<<', True),
    ('><<>', False),
]

for brackets, expected in test_cases:
    actual = correct_bracketing(brackets)
    assert actual == expected, f"Expected {expected} for brackets {brackets}, got {actual}"
```