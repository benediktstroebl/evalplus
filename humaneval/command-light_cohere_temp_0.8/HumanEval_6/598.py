```python
from typing import List


def parse_nested_parens(parent_string: str) -> List[int]:
    stack = []
    opening = False
    closing = False
    result = []
    for char in parent_string:
        if char == '(' and not closing:
            opening = True
        elif char == ')' and closing:
            closing = False
            stack.append(1)
        elif char == ')' and not opening:
            opening = True
        elif opening and closing:
            stack.append(3)
            opening = False
        elif opening:
            stack.append(1)
        elif closing:
            stack.pop()
       while(i, len(stack))
            if i == len(stack) - 2:
                result.append(stack.pop()
               i = stack.pop()
               while(i, len(stack))
                if i == len(stack) - 3:
                    result.append(stack.pop())
                   pop())
                i
            else:
                result.append(stack.pop())
                i
        print(result)
    return result

# Test cases
test_case_1 = parse_nested_parens('(()()) ((())) () ((()))()')')
print(test_case_1)  # Output: [2, 3, 1, 3]

test_case_2 = parse_nested_parens('()()((()))')
print(test_case_2)  # Output: []

test_case_3 = parse_nested_parens('((())))()')
print(test_case_3)  # Output: []

test_case_4 = parse_nested_parens('()())')
print(test_case_4)  # Output: []

test_case_5 = parse_nested_parens('((((()))))')
print(test_case_5)  # Output: [1, 3, 2]
```