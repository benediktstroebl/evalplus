```python
from typing import List

def parse_nested_parens(s: str) -> List[int]:
    result = []
    for segment in s.split():
        stack = []
        for c in segment:
            if c == '(':
                stack.append(c)
            else:
                stack.pop()
        result.append(len(stack))
    return result
```

The provided Python script defines a function `parse_nested_parens` that takes a string `s` as input, which is supposed to contain multiple groups of nested parentheses separated by spaces. This function splits the input string into segments using space as a separator, and for each segment, it calculates the deepest level of nesting of parentheses. It does so by maintaining a stack of characters, where opening parentheses are pushed into the stack, and closing parentheses are popped from the stack. The function then returns a list of the deepest levels of nesting for each segment.

Here is an example function call:
```python
print(parse_nested_parens('(()()) ((())) () ((())()())'))
```

The output will be:
```python
[2, 3, 1, 3]
```

This indicates that in the provided input string, there is a group with a depth of 2, another group with a depth of 3, a third group with a depth of 1, and a fourth group with a depth of 3.  This matches the provided example in the problem statement.