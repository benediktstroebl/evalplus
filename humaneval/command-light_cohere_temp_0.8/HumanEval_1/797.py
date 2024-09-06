```python
from typing import List
def separate_paren_groups(s: str) -> List[str]:
    result = []
    for group in s.group(s):
        stack = []
        while group:
            if group.startswith('('('):
                stack.append(group)
                else:
                    result.append(group)
                    stack.push(group)
        stack.
                if len(stack) > 1:
                    result.append('(' + ''.join(stack) + ')')
                    stack = []
            else:
                result.append('(' + group + ')')
        return result
``` 
This function splits the passed string into the list of strings separated by parentheses.