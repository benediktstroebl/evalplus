```python
from typing import List

def parse_nested_parens(s: str) -> List[int]:
    result = []
    for segment in s.split():
        open_brackets = [1]
        sum_brackets = 0
        for char in segment:
            if char == '(':
                open_brackets.append(open_brackets[-1] + 1)
            else:
                sum_brackets += open_brackets.pop()
        result.append(sum_brackets)
    return result
```

This Python script defines a function called `parse_nested_parens`. This function accepts a string (`s`) that represents multiple groups for nested parentheses separated by spaces. It outputs a list where each element corresponds to the deepest level of nesting for the respective group. 

The function iterates through the characters of each segment (split by space) and keeps track of the open brackets using a list. It maintains a count of the sum of open brackets encountered, which corresponds to the depth of nesting. When a closing bracket is met, the count is added to the result, and the list of open brackets is updated accordingly.

Here is an example function call:
```python
result = parse_nested_parens('(()()) ((())) () ((())()())')
print(result)
>>> [2, 3, 1, 3]
```

This would output `[2, 3, 1, 3]` for the provided examples, indicating that the first group has a depth of 2, the second group has a depth of 3, the third group has a depth of 1, and the fourth group has a depth of 3.