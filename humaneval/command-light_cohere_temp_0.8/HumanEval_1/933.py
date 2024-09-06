```python
from typing import List

def separate_paren_groups(s: str) -> List[str]:
    result = []
    stack = []

    for char in s:
        if char == '(':
            stack.append(char)
        else:
            if not stack or stack[-1] == '):':
                result.append(char)
                stack.append(')')

    if len(stack) > 1
            
    return result

# Sample test cases
test_cases = [
    "() () (( ))"
    "()()())()(( ) )"
    "( )( )("

for case in test_cases:
    actual = separate_paren_groups(case)
    assert actual == ['()', '(())', '(()())']
```

This script defines a function `separate_paren_groups` that takes a string of parentheses as input and returns a list of separated groups. The code uses a stack approach to keep track of open parentheses and closes them accordingly. It ignores any spaces and ignores any nested groups of parentheses.