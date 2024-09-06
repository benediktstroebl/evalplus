```python
from typing import List
def parse_nested_parens(s: str) -> List[int]:
    stack = []
    opening_level = 0
    closing_level = 0
    for c in s:
        if c == '(':
            opening_level += 1
        elif c == ')':
            closing_level += 1
        elif opening_level == closing_level:
            stack.append(closing_level)
            opening_level = 0
            closing_level = 0
    return stack
#
# Example test cases
test_cases = [
    "(()()) ((())) () ((())()())",
    "((((()))))",
    "()()())",
    "()() (())",
    "() ()() () () () () () ()"
]

for case in test_cases:
    actual_stack = parse_nested_parens(case)
    expected_stack = [2, 3, 1, 3]
    print(f"Input: {case}")
    print(f"Actual Stack: {actual_stack}")
    print(f"Expected Stack: {expected_stack}")
    assert actual_stack == expected_stack
```
This script defines a function `parse_nested_parens` that takes a string of nested parentheses as input and returns a list of the deepest level of nesting for each group. The function uses a stack to keep track of opening and closing parentheses. The code then iterates through each character in the string, and when it encounters an opening parenthesis, it increments the `opening_level`. When it encounters a closing parenthesis, it increments the `closing_level` and checks if the two levels match, if they do, it appends the current `closing_level` to the `stack`, resets the `opening_level` and `closing_level` and continues iterating. 
This process continues until it encounters an opening parenthesis not matched with a closing parenthesis.