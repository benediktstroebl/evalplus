```python
from typing import List
def separate_paren_groups(s: str) -> List[str]:
    result = []
    stack = []
    for char in s:
        if char == '(': stack.append(char)
        else:
            if not stack or stack[-1] == ')':
                result.append(char)
                stack.append(char)
        else:
                    result.append(stack.pop())
                    list(stack)
                    stack = []
    return result
# Testing function
test_cases = [
    '()()()()',
    '( )()()()',
    '(())',
    '( )',
    '( )  )',
    '(()()())',
    '()( )()'
]

for test_case in test_cases:
    actual = separate_paren_groups(test_case)
    assert actual == [('()', '(')', '(()')')]
```