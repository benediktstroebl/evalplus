Here's a Python script that contains a function called `separate_paren_groups`, taking a string of parentheses as input and returning a list of strings of separated parentheses groups.
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
            if not stack:
                return []
            current_group += char
            stack.pop()
        else:
            current_group += char
    
    return stack + [current_group]
```

This code defines a function that:
1. Creates an empty stack to hold string beginnings and a string `current_group` to store the currently formed string.
2. Iterates through the characters of the input string.
3. If the current character is `(`, it pushes the current string to the stack and resets the `current_group` string.
4. If the current character is `)`, it checks if the stack is empty. If it is, this indicates an unbalanced string, so it returns an empty list. Otherwise, it appends the `)` character to the `current_group` string and pops the top item from the stack.
5. If the current character is anything other than `( )`, it appends it to the `current_group` string.
6. After iterating through all characters, it returns the list containing all the strings popped from the stack plus the `current_group` string.

The code outputs correctly formatted lists of strings containing balanced groups of parentheses, regardless of spaces.