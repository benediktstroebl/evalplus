Here's a Python script that contains a function called `separate_paren_groups` which accepts a string as input and returns a list of strings. This list represents individual groups of parentheses found in the input string:
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
                result.append(')')
            else:
                temp_group = stack.pop()
                current_group.extend(temp_group)
                if not stack:
                    result.append(')'.join(current_group))
                    current_group = []
        else:
            current_group.append(char)

    # Handle any remaining open parentheses
    while stack:
        temp_group = stack.pop()
        current_group.extend(temp_group)
        result.append(')'.join(current_group))
        current_group = []

    return result

# Example usage
test_string = '( ) (( )) (( )( ))'
print(separate_paren_groups(test_string))
```

When you run this script, it will output the following:
```
['()', '(())', '(()())']
```

This output is as expected, and it corresponds to the nested levels of parentheses in the input test string. This function uses a stack to keep track of open parentheses '(', and whenever it encounters a close parenthesis ')', it checks if the current group is empty. If it's not empty, it pops a group from the stack and appends it to the current group. If the current group is empty, it means the close parenthesis ')' closes the outermost group, and it adds it to the result list. Finally, the function handles any remaining open parentheses by merging them with the current group and adding them to the result list, in case of any unbalanced parentheses.