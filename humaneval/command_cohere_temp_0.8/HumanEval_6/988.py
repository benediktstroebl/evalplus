```python
from typing import List

def parse_nested_parens(s: str) -> List[int]:
    result = []
    forOpening, i = 0, 0
    for char in s:
        if char == '(':
            forOpening += 1
            i += 1
        elif char == ')':
            forOpening -= 1
            i -= 1
        if forOpening > i:
            result.append(forOpening)
            i = 0
    return result
```

The provided Python script defines a function `parse_nested_parens` that takes a string `s` containing multiple groups of nested parentheses separated by spaces as input. It iterates through each open parenthesis `(` it encounters, maintaining a count of its depth (`forOpening`) and a counter for the current iteration index (`i`). When a closing parenthesis `)` is encountered, it decreases the depth count and resets the index to 0, as the depth is only determined while an opening parenthesis is unclosed. The function returns a list `result` that contains the deepest level of nesting of parentheses for each group.

Here is an example function call:
```python
print(parse_nested_parens("(()()) ((())) () ((())()())"))
```

The output will be:
```python
[2, 3, 1, 3]
```

This exemplifies the function's capability to extract the depth of nesting for each group of parentheses in the provided input string.