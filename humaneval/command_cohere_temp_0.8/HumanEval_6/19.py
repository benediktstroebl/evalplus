```python
from typing import List

def parse_nested_parens(s: str) -> List[int]:
    result = []
    for opener, closer in zip('([{', ')]}'):
        stack = [0]
        level = 0
        for ch in s:
            if ch == opener:
                stack.append(level)
            elif ch == closer:
                level = stack.pop()
                if stack:
                    result.append(max(level, stack[-1]))
            else:
                level += 1
        if stack:
            result.append(max(level, stack[-1]))
    return result
```

The approach uses a straightforward nested iteration over the input string. It maintains a stack of the maximum depths of open brackets encountered so far, and a running total of the current depth. When a closing bracket is encountered, the running total is popped if it is greater than the current maximum, otherwise, it is added to the stack. The result is the maximum depth of each nested group. 

The tests provided in the problem statement can be replicated as follows: 
```python
test_strings = [
    '(()()) ((())) () ((())()())',
    '(())',
    '((()))',
    '(()()())',
    '([{}])',
    '({[]})',
    '([())',
    '({()}())',
    '{{[()}}]',
]

for expect, test in zip(
    [2, 3, 1, 3, 2, 1, 3, 2, 1, 1], 
    test_strings
):
    print(f'\n >>> parse_nested_parens("{test}") [[{expect}]]')
    assert parse_nested_parens(test) == [expect]
``` 

This replicates the example provided in the problem statement and adds a few more test cases to ensure that the function behaves correctly for other interesting cases.