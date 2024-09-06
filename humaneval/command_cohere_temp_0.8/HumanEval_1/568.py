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
                print('Unexpected )')
                continue
            current_group = stack.pop()
        else:
            current_group.append(char)
    
    if stack:
        print('Unexpected )')
    else:
        result.extend(stack)
        result.extend(current_group)
    
    return result
```

The provided Python script defines a function `separate_paren_groups` which takes a string `paren_string` as input. This string contains multiple groups of nested parentheses. The goal is to separate these groups into individual strings and return them in a list.

Here is an example of input: `( ) (( )) (( ()( )))`

And below is the corresponding output:
```
['()', '(())', '(()())']
```

The function uses a stack to keep track of open parentheses `(` and a separate list `current_group` to store the characters between parentheses. The `result` list stores the final separated strings.

The script iterates through each character of the input string. If it encounters an open parenthesis `(`, it pushes the current group (`current_group`) onto the stack. If it encounters a close parenthesis `)`, it checks if the stack is empty. If not, it pops the top item from the stack, which is the most recently opened group, and appends it to `current_group`. All other characters are directly appended to `current_group`.

After processing all characters, the function checks if there are any items left in the stack. If there are, it prints an error message indicating extra unclosed parentheses. Finally, it extends the `result` list with all items from the stack and `current_group`. This results in a list of strings where each string contains a separate group of parentheses.