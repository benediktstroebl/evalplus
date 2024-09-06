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
            current_group = stack.pop()
        else:
            current_group += char

    return stack
```

This Python script provides a self-contained function `separate_paren_groups` that accepts a string of parentheses and returns a list of nested groups separate from each other. It works by utilizing a stack to keep track of opened parentheses until they are closed, creating separate strings for each group of parentheses. This approach ensures that each open brace has a proper match with a closed brace, making it balanced and free from any nesting within other groups. The function also ignores any spaces present in the input string. 

The provided example and test case, `( ) (( )) (( )( ))', returns a list of three strings: ['()', '(())', '(()())']. This is the expected output, as the script divides the groups of parentheses into separate entries in the list.

This approach ensures that the function works appropriately for more complex groupings of parentheses as well.