```python
from typing import List

def parse_nested_parens(s: str) -> List[int]:
    result = []
    for bracket_level in map(len, s.split(' ')):
        result.append(bracket_level)
    return result
```

The specified Python script solves the problem of parsing nested parentheses in a given string. The `parse_nested_parens` function takes a single argument `s`, which is the input string containing multiple groups of nested parentheses separated by spaces. 

The function uses a list `result` to store the output. It iterates over the string splits into multiple parts using spaces as separators. In each iteration, it calculates the length of nested parentheses group (i.e., the number of opening and closing parentheses) using the `len` function and appends this value to the `result` list. 

Finally, the function returns the `result` list, which provides the deepest level of nesting for each group of parentheses in the input string. 

This solution is efficient and has a time complexity of O(n), where n is the number of groups of parentheses in the input string.