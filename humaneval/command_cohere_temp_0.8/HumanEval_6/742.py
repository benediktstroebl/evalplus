```python
from typing import List

def parse_nested_parens(s: str) -> List[int]:
    result = []
    for nested_parens in s.split():
        current_level = 0
        nested_count = 0
        for char in nested_parens:
            if char == '(':
                nested_count += 1
                current_level = max(current_level, nested_count)
            elif char == ')':
                nested_count -= 1
        result.append(current_level)
    return result
```

This script includes a function called `parse_nested_parens` that takes in a string `s` containing multiple groups of nested parentheses separated by spaces, and returns a list where each element represents the deepest level of nesting of parentheses in each group. The function uses a loop to iterate through each nested group of parentheses, maintaining a `current_level` variable to keep track of the current maximum nested count, and increments or decrements the `nested_count` variable depending on the encountered parentheses or parentheses. The `result` list is then populated with the `current_level` for each group, representing the deepest level of nesting for each group of parentheses.