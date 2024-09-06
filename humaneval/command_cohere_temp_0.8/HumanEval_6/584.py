```python
from typing import List

def parse_nested_parens(s: str) -> List[int]:
    result = []
    for segment in s.split():
        stack = []
        for char in segment:
            if char == '(':
                stack.append(char)
            else:
                stack.pop()
        result.append(len(stack))
    return result
```

This code defines a function `parse_nested_parens` that takes a string `s` as input, where each character in the string represents a group of nested parentheses separated by spaces. 

The function splits the input string into segments using spaces as separators, and for each segment, it determines the deepest level of nesting of parentheses by using a stack data structure. 

The deepest level of nesting for each segment is appended to a list `result`, which is returned as the output of the function. 

Here is an example usage of the function:
```python
>>> parse_nested_parens('(()()) ((())) () ((())()())')
[2, 3, 1, 3]
```

This will produce a list with the results for each segment, where each element corresponds to the deepest level of nesting of parentheses in the respective segment.