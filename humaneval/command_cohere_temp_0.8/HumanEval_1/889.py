Here's a Python script that contains a function called `separate_paren_groups`, which takes a string of parentheses as input and returns a list of separate groups of parentheses. 

The function works by using the `reversed` function to iterate through the input string from the end to the beginning. By doing this, the function can detect when a closing parenthesis is encountered that corresponds to an opening parenthesis. The function uses a stack to keep track of nested parentheses and appropriately handles nested and balanced groups. When a closing parenthesis is encountered, the function checks if it matches the most recent opening parenthesis. If it does not, then the closing parenthesis must belong to the next group, so the current group is reversed and pushed to the stack. If it does match, then the group is reversed and pushed to the list of results, and the stack is popped to continue processing the next group. The function finishes when all the parentheses have been processed.

```python
import string
from typing import List

def separate_paren_groups(paren_string: str) -> List[str]:
    stack = []
    results: List[str] = []
    for char in reversed(paren_string):
        if char in string.punctuation and char != ' ':
            if not stack or paren_string[len(stack) - 1] != '(':
                results.append(''.join(stack))
                stack = []
            stack.append(char)
        elif char == ')':
            if not stack:
                results.append('')
            elif paren_string[len(stack) - 1] == '(':
                stack.pop()
            else:
                results.append(''.join(stack))
                stack = []
    return results + [(''.join(stack))]
```