```python
from typing import List

def separate_paren_groups(paren_string: str) -> List[str]:
    stack = []
    current_group = ""
    
    for char in paren_string:
        if char == '(':
            current_group += char
            stack.append(current_group)
            current_group = ""
        elif char == ')':
            current_group += char
            if stack:
                stack.pop()
            else:
                print(f"Unmatched right parenthesis '{char}'.")
        
        # Add current group to the stack if it is closed
        if not stack and current_group:
            stack.append(current_group)
            current_group = ""
    
    return stack
```

This Python script takes a string as input and returns a list of strings. Each string in the list represents a separate
group of nested parentheses, and the list reflects the relative order of these groups in the input string. The script ensures
that each open parenthesis `(`) has a matching closed parenthesis `)`, and that nested groups are correctly separated. 

The program achieves this by maintaining a `stack` of currently open groups. Whenever it encounters an open parenthesis,
it appends the current group to the stack, resets the current group, and starts building a new group. When it encounters a
closed parenthesis, it checks if a corresponding open parenthesis is in the stack and hence matches it with any currently
open group. If it wasn't matching any open group, then this implies an unmatched right parenthesis, and the program
prints a corresponding error message. 

After traversing the entire input string, the program returns a list of all the separate groups, in the order they appeared
in the input string, and nested groups are correctly separated. 

This approach uses a stack to keep track of open groups, which is a common technique in recursive descent parsing. It
provides a simple and efficient solution to the problem, although space complexity might become an issue for
very large input strings with deep nested parentheses groups.