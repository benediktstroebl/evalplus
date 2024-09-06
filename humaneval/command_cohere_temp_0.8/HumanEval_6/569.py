```python
from typing import List

def parse_nested_parens(s: str) -> List[int]:
    result = []
    for nested_parens in s.split():
        current_level = 0
        for char in nested_parens:
            if char == '(':
                current_level += 1
            elif char == ')':
                current_level -= 1
        result.append(current_level)
    return result
```

The specified Python script solves the problem of determining the deepest level of nesting of parentheses in a given string. It does this by using a simple loop to iterate through each nested group of parentheses, keeping track of the current nesting level with a counter. It then appends each group's maximum nesting level to a list of results and finally returns the list.

This approach has a time complexity of O(n), where n is the number of characters in the input string, as it requires iterating through each character in the string once. It is an efficient and straightforward solution to the problem.