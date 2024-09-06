Here is a self-contained Python script that solves the problem of separating nested parentheses into separate groups:
```python
def separate_paren_groups(s):
    return ['(' + c + ')' for c in s.
    if not c:
        return []
    return [c] + separate_paren_groups(s[1:])

# Test case
test_cases = [
    "())",
    "(())",
    "( )(( )) )",
    "((()))",
    "((()))()",
    "((()))()()",
    "( (( )) )",
    "( (  )) )",
    "(( ) ) )",
    "()()()()",
]

for test_case in test_cases:
    actual = separate_paren_groups(test_case)
    assert actual == test_case.
```

This code defines a function called `separate_paren_groups` that takes a string `s` as input and returns a list of strings created by splitting parenthesis groups. The `assert` statement is used to check if the output of the function matches the expected result.