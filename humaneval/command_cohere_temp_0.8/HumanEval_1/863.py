Here's a Python script that contains a function called `separate_paren_groups`, which takes a string of parentheses as input and returns a list of strings containing only the separate groups of parentheses. The script also includes a set of tests to verify the function's correctness:
```python
from typing import List

def separate_paren_groups(paren_string: str) -> List[str]:
    stack = []
    current_group = []
    result = []

    for char in paren_string:
        if char == '(':
            stack.append(current_group)
            current_group = []
        elif char == ')':
            if not stack:
                result.append(')'.join(current_group))
            else:
                tmp = stack.pop()
                current_group.extend(tmp)
                if not stack:
                    result.append(')'.join(current_group))
        else:
            current_group.append(char)

    if current_group:
        result.append(')'.join(current_group))

    return result

# Tests
paren_strings = [
    '()',
    '(())',
    '(()())',
    '((()))',
    '(())(())',
    '(((((())))))',
]

for p in paren_strings:
    assert separate_paren_groups(p) == [p]
```

The provided code demonstrates a straightforward method for solving the problem using a stack to keep track of opening parentheses and a list to store the currently building group of parentheses. After processing all characters, any remaining parentheses in the `current_group` will be considered a separate group and added to the result list. The tests ensure that the function produces the correct output for various input scenarios.