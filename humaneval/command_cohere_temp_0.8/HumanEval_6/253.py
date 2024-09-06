```python
from typing import List

def parse_nested_parens(s: str) -> List[int]:
    result = []
    for opened, closed in zip(*[iter(s.split())] * 2):
        count = opened.count(opened[0]) - closed.count(closed[0])
        result.append(count)
    return result
```

The provided Python script solves the problem of parsing nested parentheses and returns a list of depths of each group in the input string. The function `parse_nested_parens` takes a string as input and iterates through the opened and closed parentheses groups, counting the number of opening parentheses minus the number of closing parentheses to determine the depth of each group. The result is then appended to a list.

To achieve this, the script uses the `zip` function to iterate through each of the opened and closed parentheses groups, taking advantage of the splitting of the input string by spaces. For each group, it calculates the depth by counting the number of opening parentheses and subtracting the number of closing parentheses, providing the depth of nesting. The resulting depths for each group are collected in the `result` list, which is returned.

This approach allows the script to efficiently parse the input string and accurately determine the depths of each group of nested parentheses, providing a reliable solution for the problem.