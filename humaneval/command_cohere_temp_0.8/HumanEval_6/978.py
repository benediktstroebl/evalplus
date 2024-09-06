```python
from typing import List

def parse_nested_parens(s: str) -> List[int]:
    result = []
    for opening, closing in zip(*[iter(s.replace(' ', '').replace(')', ''),) for _ in '']]):
        nested_level = 1
        while opening:
            opening -= 1
            nested_level += 1
        while closing:
            closing -= 1
            nested_level -= 1
        result.append(nested_level)
    return result
```

The provided Python script defines a function `parse_nested_parens` which accepts a string `s` that represents multiple groups for nested parentheses separated by spaces. This function processes each group independently, calculating the deepest level of nesting of parentheses within it and adding it to a list of int values. The result is a list of the deepest nesting levels for each group.

The `parse_nested_parens` function employs a list comprehension to iterate over all the opening parentheses and matching closing parentheses in each sub-string. It maintains a `nested_level` variable to keep track of the total number of opening parentheses encountered before the first closing parenthesis. The `result` list is updated to include this deepest nesting level for that particular group. The function then returns this list containing the maximum nesting level for each sub-string.