```python
def parse_nested_parens(paren_string: str) -> List[int]:
    stack = []
    stack_top = 0
    output = []
    for char in paren_string:
        if char == "(":
            stack.push(stack_top)
            stack_top += 1
        elif char == ")":
            stack_top = stack.pop()
           if (stack_top == 0):
                output.append(stack_top)
            stack_top = 0
    return output

# Example:
test_cases = [
    "(()()) ((())) () ((())())",
    "((())) () () ((())()())",
    "(((((())))))",
    "(())() ((()))",
    "()()() ()",
    "() ()() ()() ()",
]

for test_case in test_cases:
    actual_output = parse_nested_parens(test_case)
    assert actual_output == [2, 3, 1, 3], f"Invalid output: {actual_output}"
```

This code defines a function `parse_nested_parens` that takes a string of nested parentheses as input and returns a list of the deepest levels of nesting. The `test_cases` list contains a variety of test cases, and the code includes a test loop that iterates through these cases, calling the function with each test case. The output of the code is then checked against the expected output using the `assert` statement, with any discrepancies displayed using the `f-string` formatting.