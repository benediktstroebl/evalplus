```python
def parse_nested_parens(paren_string: str) -> List[int]:
    stack = []
    open_parens = {}
    closed_parens = {}
    level = 0

    for char in paren_string:
        if char == ')':
            if open_parens.get(level, 0):
                stack.append(level)
                level += 1
                open_parens[level] = 0
            else:
                closed_parens[level] = stack.append(level)
                stack.append(0)
        if level > 0:
            level -= 1

    return stack

# Example usage
test_cases = [
    ("(()())((()))",
    ("(()()))((())))",
    ("()()()()((()))",
    ("(()()())()()()()()()()())",
    ("())()()()()()()()()()()",
]

for case in test_cases:
    assert parse_nested_parens(case) == [2, 3, 1, 3]
``` 
This script defines a function `parse_nested_parens` that takes a string of nested parentheses as input and returns a list of the deepest level of nesting for each group of parentheses.  The test cases with various nested parentheses and the function's output is compared against the expected result using `assert`.  The test cases cover various scenarios with different levels of nesting.