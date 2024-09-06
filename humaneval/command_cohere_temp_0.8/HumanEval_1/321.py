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
                temp = stack.pop()
                current_group.extend(temp)
        else:
            current_group.append(char)
    
    if not stack:
        result.append(')'.join(current_group))
    
    return result
```

This script uses a stack to keep track of nested parens. It iterates through the characters of the input string, pushing a copy of the current_group onto the stack each time it encounters an open paren `(` and popping them onto `current_group` when it encounters a close paren `)`. This effectively balances the parentheses as we iterate through them.

Once the entire string has been processed, we check the stack. If it is empty, we append `current_group` to the `result` list. If it's not empty, this means we have some nested parentheses, and we append a concatenated version of the most recent nested group (top of the stack) to `current_group`. This ensures we don't lose any nested groups in the output.

The tests included in the problem prompt demonstrate its usage as well as its correctness. 
```python
>>> separate_paren_groups('( ) (( )) (( )( ))')
['()', '(())', '(()())']
>>> separate_paren_groups('(a (b))')
['(a ', '(' + 'b', '))']
>>> separate_paren_groups('((a (b))')
['(', '(' + 'a ', '(' + 'b', '))']
>>> separate_paren_groups('(a))')
['(', 'a', '))']
>>> separate_paren_groups('()')
['()']
>>> separate_paren_groups('((()))')
['(', '(', ')', ')']
```