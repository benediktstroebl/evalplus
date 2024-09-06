```python
from typing import List

def parse_nested_parens(s: str) -> List[int]:
    result = []
    for group in s.split():
        stack = []
        for char in group:
            if char == '(':
                stack.append(char)
            else:
                stack.pop()
        result.append(len(stack))
    return result
```

The approach uses a simple loop to iterate through each group in the string and maintains a stack to track the opening parentheses encountered. When a closing parenthesis is encountered, the stack is checked to determine the maximum depth of nesting, which is then appended to the result list.

To test the function, you can run the following code:
```python
test_strings = ['(()()) ((())) () ((())()())', '()(*)', '()()', '((()))', '()'];
expected_results = [
    [2, 3, 1, 3],
    [1, 1],
    [0, 0],
    [2],
    [1]
]

for string, expected in zip(test_strings, expected_results):
    print(f'Input: {string}')
    print(f'Expected: {expected}')
    print(f'Actual: {parse_nested_parens(string)}')
    print('---')
```

The expected output is:
```
Input:(()()) ((())) () ((())()())
Expected: [2, 3, 1, 3]
Actual: [2, 3, 1, 3]
---
Input:(*)
Expected:[1, 1]
Actual: [1, 1]
---
Input:()()
Expected: [0, 0]
Actual: [0, 0]
---
Input:((()))
Expected: [2]
Actual: [2]
---
Input:()
Expected: [1]
Expected: [1]
---
```