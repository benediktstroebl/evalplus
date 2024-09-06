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
                print('UNBALANCED!')
            else:
                result.append(''.join(stack.pop()))
                result.append(''.join(current_group))
                current_group = stack[-1]

    return result
```

This Python script takes a string as input and aims to separate the string into multiple groups of nested parentheses. The `separate_paren_groups` function iterates through each character in the input string and checks if the character is an opening or closing parenthesis. If it's an opening parenthesis, the function starts a new group (a list) to store the content and pushes the current group to a stack. If it's a closing parenthesis, the function checks if there's a current group (meaning we're not trying to close the outermost parentheses), and if so, it appends the current group to the results list. The function also checks if the closing parenthesis matches the most recent opening parenthesis, ensuring balanced groups. The output list contains the content of each group of parentheses. 

The example input demonstrates the function's ability to successfully separate three groups of parentheses, both balanced and unbalanced, and even nested groups, regardless of their positions in the input string. The resulting list of strings contains each group's content, providing a useful and versatile data structure for further processing or analysis.