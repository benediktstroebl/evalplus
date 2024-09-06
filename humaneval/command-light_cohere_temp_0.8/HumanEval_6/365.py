```python
from typing import List
def parse_nested_parens(s: str) -> List[int]:
    stack = []
    in_string = False
    result = []
    for char in s:
        if char == "(":
            if not in_string:
                stack.append(1)
                in_string = True
        elif char == ")":
            if len(stack) > 0 and stack.pop() == 1:
                in_string = False
            else:
                stack.append(0)  # Place holder for the next opening parent
        else:
            in_string = False
            continue
    if len(stack) > 0:
        in_string = False
    return result
# Example test cases
test_case1 = "(((())))()((()))()((()))"
test_case2 = "(((((()))))))))"
test_case3 = "((()))()())(((()))"

# Function call with test cases
result = parse_nested_parens(test_case1)
print(result)
result = parse_nested_parens(test_case2)
print(result)
result = parse_nested_parens(test_case3)
print(result)
```