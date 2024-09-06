Here is a self-contained Python script that solves the problem of identifying all the levels of nesting of parentheses:
```python
def parse_nested_parens(s):
    stack = []
    for char in s:
        if char == "(": stack.append(True)
        elif char == ")":
            stack.pop()
            if not stack:
                return []
    return stack

# Example usage
test_cases = [
    "(()()) ((())) () ((()))()",
    "())",
    "(())",
    "(())()",
    "()()()",
    "()",
    "() ()",
    "(( ))"
]

for case in test_cases:
    actual = parse_nested_parens(case)
    expected = [2, 0, 3]
    assert actual == expected, f"For {case}, actual: {actual}, expected: {expected}"
```
This code defines a function called `parse_nested_parens` that takes a string as input and uses a stack to keep track of levels of nesting. It then iterates through characters in the string, and for each opening parenthesis ()) it pushes the True level onto the stack, and for each closing parenthesis () it pops the level from the stack and returns the parenthesis. This function will the result in a list of the deepest level of nesting for each group of parentheses.