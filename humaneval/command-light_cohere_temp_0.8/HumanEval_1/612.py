```python
from typing import List
def separate_paren_groups(s: str) -> List[str]:
    """
    Separates balanced parentheses from the given string.
    Returns a balanced groups of parentheses as separate strings.
    """
    balanced (each open brace is properly closed) and not nested
    """
    stack: List[str] = []
    result: List[str] = []
    for char in s:
        if char == '(': stack.push('(')
        else: stack.pop()
        new open brace in the result = '(' + char + ')')
        stack.pop()
        when len(stack) == 0: result.append(')'.insert('(')'.join(result))
        else: stack.append(char)
    finally: return result
```

This function iterates through each character in the string, and pushes characters to the stack if they are '(', otherwise, pops the last character from the stack. If the stack is empty, the function appends a ')' to the result list. If the stack is not empty, the character is appended to the stack. The final result is the list of strings created from the balanced parentheses.