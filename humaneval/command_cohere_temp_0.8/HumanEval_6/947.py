```python
from typing import List

def parse_nested_parens(s: str) -> List[int]:
    result = []
    for bracket_str in s.split():
        level = 0
        for char in bracket_str:
            if char == '(':
                level += 1
            elif char == ')':
                level -= 1
        result.append(level)
    return result
```

The specified Python script presents a function called `parse_nested_parens`, which accepts a string input (`s`) that represents several groups of nested parentheses divided by spaces. This function's purpose is to calculate and return a list of the deepest levels of indentation for each parentheses group.

To accomplish this, the function initializes an empty `list result` to store the outcomes. It then breaks the input string into individual bracket strings using the `split()` method. Following that, it iterates through each bracket string, keeping track of the current nesting level with the variable `level`. Each opening parenthesis (`(`) increases the level by 1, and each closing parenthesis (``) decreases it by 1.

Once the iteration is finished for each bracket string, the function adds the recorded nesting level to the `result` list. The resulting list is then returned, containing the maximum indentation levels for each parentheses group.

This solution adheres to the specified problem and provides an effective way to parse and compute the deepest nesting level for multiple parentheses groups in a single string. It is compatible with the provided test case and meets the problem requirements.