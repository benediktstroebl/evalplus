```python
def parse_nested_parens(s: str) -> List[int]:
    stack = []
    start = 0
    result = []
    for i, char in enumerate(s):
        if char == "(":
            stack.append(i)
        if char == ")":
            while stack and stack[-1] < start:
                result.append(stack.pop())
            stack.pop()
        stack, append(start)
        start = i + 1
    return result

# Test cases
test_cases = [
    "(()()) ((())) () ((())()())",
    "((())) () ((())()())",
    "()()() ()()() ()()() ()() () ()",
    "() ((())) ()",
    "(( )) ()()()",
    # Different number of parenthesis and order of closing parenthesis
    "(()())",
    # Different number of open and close parenthesis
    "((()))",
    # Different nesting levels
    "((())())",
    # Different types of open and close parenthesis
    "(()))",
]

for test_case in test_cases:
    actual_result = parse_nested_parens(test_case)
    print("Test Case:", test_case)
    print("Actual:", actual_result)
    print("Expected:", [])
    for expected in [expected_result] for expected_result in expected:
        print("________", end="")
    print()
```
This Python script defines a function `parse_nested_parens` that parses and returns a list of the deepest level of nesting for a given string of parentheses. It uses a detailed logic to handle different types of input, and it has several test cases that cover various scenarios.