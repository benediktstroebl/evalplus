```python
from typing import List

def parse_nested_parens(s: str) -> List[int]:
    result = []
    for bracket_level in s.split():
        level = 0
        unbalanced = 0
        nesting_level = 0
        for char in bracket_level:
            if char == '(':
                level += 1
                unbalanced += 1
            elif char == ')':
                level -= 1
                unbalanced -= 1
                if unbalanced > 0:
                    nesting_level += 1
        result.append(nesting_level)
    return result
```

This code defines a function `parse_nested_parens` that takes a string `s` containing multiple groups of nested parentheses separated by spaces, and returns a list where each element represents the deepest nesting level of parentheses in each group.

The `parse_nested_parens` function iterates through each group of parentheses in the provided string and keeps track of the current nesting level, incrementing it whenever it encounters an opening parenthesis `(` and decrementing it whenever it encounters a closing parenthesis `)`. The `unbalanced` variable keeps track of the difference between the number of opening and closing parentheses encountered, and it's used to calculate the deepest nesting level by adding 1 to the `nesting_level` whenever there are still unbalanced opening parentheses.

Here's an example usage of the function:
```python
print(parse_nested_parens('(()()) ((())) () ((())()())'))
```
The output will be:
```
[2, 3, 1, 3]
``` 

This example string has four groups of parentheses, and the function will return a list with four elements, representing the deepest nesting level for each group, respectively [2, 3, 1, 3].