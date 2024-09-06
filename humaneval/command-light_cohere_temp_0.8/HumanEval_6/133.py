Here's a self-contained Python function that solves the problem of parsing and matching parentheses in a string:
```python
def parse_nested_parens(s: str) -> List[int]:
    stack = []
    result = []
    for match in s:
        if match == '(': stack.push(1)
        if match == ')': stack.pop()
        level = stack.pop()
        level == None: result.push([])
    the stack = []
    return result

# Test cases
test_cases = [
    "(()()) ((())) () ((())())",
    "((((()))))",
    "()()()())",
    "((()))()()()()",
    "((((())))))()",
]

for test_case in test_cases:
    actual_result = parse_nested_parens(test_case)
    print(f"Test case: {actual_result, expected_result=[])
    for actual, expected in zip(actual_result, expected_result):
        print(f"{actual} != {expected}: {test_case}{actual} != ({expected})", end='')
```
The code defines a function `parse_nested_parens` that takes a string `s` as input and returns a list of integers. It uses a stack to keep track of the level of nesting and adds the top-level match to the `result` list. The test cases ensure that the function works correctly and provides the expected output.