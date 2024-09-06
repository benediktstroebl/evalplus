Here is a self-contained Python script that solves the problem you described:
```python
from typing import List
def parse_nested_parens(parentheses_string: str) -> List[int]:
    stack = []
    result = []
    for parantheses in parentheses_string.t:
      if len(parantheses) == 0:
          stack.push(len())
      else:
          stack.append(parantheses)
          stack = [a for a in stack if a != '(']
          result.append(len(stack)
      return result
```
This function takes a string of nested parentheses as input and returns a list of the deepest levels of nesting for each group of parentheses in the string. It uses a stack to keep track of open parentheses while iterating through the string.

The function uses a list comprehension to only add closed parentheses to the stack, as any open parentheses need to be expanded before we can consider the current group as a finished group.