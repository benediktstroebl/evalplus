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
                print('WRONG')
            else:
                result.append(''.join(stack.pop()))
                result.append(''.join(current_group))
                current_group = stack[-1]
        else:
            current_group.append(char)

    if not stack:
        result.extend(current_group)
    else:
        print('WRONG')

    return result
```

The algorithm utilizes a stack to keep track of nested parentheses groups. It turns out that given the current character and the stack, we can easily determine whether the current character is opening or closing and also whether the stack is currently expecting an opening or closing parenthesis. You can easily see why this is the case by drawing a parenthesis diagram and noting what values you would expect in each case.

The stack serves as an abstract “stack” of parentheses that is, it metaphorically represents a stack of parentheses from the input string. Whenever we encounter an opening parenthesis, we “push” it (onto the stack). Whenever we encounter a closing parenthesis, we check whether an opening one is expecting (i.e. whether the current top of the stack is an opening parenthesis). If it is, we “pop” it (from the stack).

We start with an empty stack and push all opening parentheses. When we encounter the first closing parenthesis, we will have a stack with a single element (the opening parenthesis we started with). We pop it and yield it to the result. Then we push the closing parenthesis onto the stack and continue with the next iteration. The next closing parenthesis will match the most recent opening parenthesis on the stack, and so forth. The algorithm will correctly separate the parentheses into nested groups.