Here's a Python script with a self-contained function that solves the problem using a stack to keep track of opening parentheses encountered:
```python
from typing import List

def parse_nested_parens(s: str) -> List[int]:
    result: List[int] = []
    stack: List[int] = []

    for char in s:
        if char == '(':
            stack.append(len(stack))
        else:
            if not stack:
                result.append(0)
            else:
                stack.pop()
                result.append(len(stack))

    if stack: 
        result.append(len(stack))

    return result
```

The `parse_nested_parens` function uses a stack to keep track of open parentheses encountered and increments the level for each open parenthesis added to the stack and decrements the level when a close parenthesis is encountered and removed from the stack. The result list is then populated with the final nesting level for each group of parentheses.

This approach allows to efficiently compute the nesting level of each group of parentheses in the given string in a single pass.

To test this function, you can run the following code:
```python
test_strings = [
    '(()()) ((())) () ((())()())',
    '((()))',
    '(()())',
    '(((((((()())]))))))',
    '()',
    '((()))',
    '(((())))',
    '()()()',
]

for string in test_strings:
    print(f"Input: {string}")
    expected_result = [2, 3, 2, 3, 5, 1, 2, 3, 2]
    calculated_result = parse_nested_parens(string)
    assert calculated_result == expected_result, f"Expected {expected_result}, got {calculated_result}"
``` 

This will demonstrate the functionality of the function with different input scenarios and expected outputs.