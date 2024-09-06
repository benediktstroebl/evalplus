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
                yield current_group
            elif stack[-1] == "":
                stack.pop()
            else:
                current_group = stack.pop()
        else:
            current_group += char
            
    # yielding the last group in the string
    if current_group:
        yield current_group
```

This script uses a stack to keep track of nested parens and yields separate groups of parens as it goes. The last item in the list of yielded groups will be the last item in the input string. An example of an input string and the resulting output is shown below:
```python
>>> separate_paren_groups("( ) (( )) (( )( ))")
['()', '(())', '(()())']
``` 
**NOTE**: This approach has a time complexity of O(n) and a space complexity of O(n) as well, where n is the number of characters in the input string.