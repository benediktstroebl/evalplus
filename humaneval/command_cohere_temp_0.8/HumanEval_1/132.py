Here's a Python script that contains a function called `separate_paren_groups`, which takes a string of parentheses as input and returns a list of separate groups of parentheses.
```python
from typing import List

def separate_paren_groups(paren_string: str) -> List[str]:
    stack = []
    current_group = ""

    for char in paren_string:
        if char == '(':
            stack.append(current_group)
            current_group = ""
        elif char == ')':
            current_group += char
            if not stack:
                return []
            top_group = stack.pop()
            if not top_group:
                result.append(current_group)
            else:
                current_group = top_group + current_group
        else:
            current_group += char

    return result

# Sample input and expected output
input_string = '( ) (( )) (( )( ))'
expected_output = ['()', '(())', '(()())']

result = separate_paren_groups(input_string)
print(f"Output: {result}")
assert result == expected_output
```
This script uses a stack to keep track of nested parentheses groups. When an opening parenthesis is encountered, it pushes the current group (if any) onto the stack and starts a new group. When a closing parenthesis is encountered, it pops the last group from the stack, merges it with the current group, and adds the resulting group to the output list. If the stack is empty, the last group encountered is added to the output. Finally, the script outputs the list of separated parentheses groups.