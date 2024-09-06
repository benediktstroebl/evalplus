```python
def parse_nested_parens(s: str) -> List[int]:
    stack = []
    levels = []
    nesting = True
    for c in s:
        if c == '(':
            nesting = True
        elif c == ')':
            nesting = False
        else:
            stack.push(c)
            if nesting:
                levels.append(len(stack))
                stack = []
    return levels

# Test cases
test_cases = [
    ("()() ((())) () ((())()())"),
    ("())()(())(())()())",
    ("(())()(()())()())",
    ("()() )))()",
    ("()()()()()()()()",
]

# Test function
for tc, test_str in test_cases:
    actual_levels = parse_nested_parens(test_str)
    expected_levels = [2, 3, 1, 3]  # Test expected values
    if actual_levels != expected_levels:
        print(f"Test case {tc} failed.")
    else:
        print(f"Test case {tc} passed.")
```
This code provides a function `parse_nested_parens` that takes a string as input and returns a list of integers representing the deepest level of nesting of parentheses in the string. The function uses a stack to keep track of opening parentheses and a list `levels` to keep track of the deepest levels of nesting. The function iterates over the levels and pushes characters onto the stack when they are '(', and pops them off when they are ')'. The function then returns the list `levels` which contains the deepest levels of nesting in the string.