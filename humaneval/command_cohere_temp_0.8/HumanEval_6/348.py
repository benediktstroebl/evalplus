```python
from typing import List

def parse_nested_parens(s: str) -> List[int]:
    result = []
    for chunk in s.split(' '):
        stack = []
        for char in chunk:
            if char == '(':
                stack.append(char)
            else:
                stack.pop()
        result.append(len(stack))
    return result
```

This Python script can be translated directly into Markdown code using backticks (` `):
```
```python
from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())()) () ((())()())')
    [2, 3, 1, 3]
    """

    result = []
    for chunk in paren_string.split(' '):
        stack = []
        for char in chunk:
            if char == '(':
                stack.append(char)
            else:
                stack.pop()
        result.append(len(stack))

    return result
```

This solution has the same logic as the original Python script provided in the prompt, but it is now encapsulated within a Markdown code block within double backticks (` `` ``). 
This script solves the problem by splitting the input string into space-separated chunks and then parsing each chunk separately to determine the deepest level of nesting of parentheses. The `stack` is used to keep track of the number of opening parentheses `(` and is incremented each time an opening parenthesis is encountered and decremented each time a closing parenthesis `)` is encountered. The deepest level of nesting is determined by the length of the stack once all chunks have been processed.