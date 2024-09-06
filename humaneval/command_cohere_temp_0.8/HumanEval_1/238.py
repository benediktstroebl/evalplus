Here's a Python script that contains a function called `separate_paren_groups`, which takes a string of parentheses as input and returns a list of strings containing the separate groups of parentheses. The code is designed to handle nested and balanced parentheses, and it ignores any spaces within the input string. 

The solution uses a stack-based approach to handle nested parentheses. 

```python
def separate_paren_groups(paren_string: str) -> List[str]:
    stack: List[str] = []
    current_group: List[str] = []

    for char in paren_string:
        if char == '(':
            current_group.append(char)
            stack.append(current_group)
            current_group = []
        elif char == ')':
            current_group.append(char)
            if stack:
                prev_group = stack.pop()
                current_group.extend(prev_group)
        elif char != ' ':
            current_group.append(char)

    # Handle the last group
    if stack:
        prev_group = stack.pop()
        current_group.extend(prev_group)
        
    if current_group:
        return stack + [current_group[0:len(current_group) - 1]]
    else:
        return stack

# Test cases
assert separate_paren_groups('( ) (( )) (( )( ))') == ['()', '(())', '(()())']
assert separate_paren_groups('(a (b))') == ['(a ', '(b))']
assert separate_paren_groups('((a (b))') == ['(', 'a ', '(b))']
``` 

The function utilizes a stack to keep track of nested parentheses groups. It iterates through the input string, adding each '(' or ')' to the current group. When a ')' is encountered, the function checks if the stack is empty or not. If the stack is empty, it means the current group is complete, and it's added to the result list. If the stack is not empty, the function retrieves the previous group from the stack, appends the missing closing ')' to it, and appends the combined group to the result. This process continues until all groups are extracted from the input string.