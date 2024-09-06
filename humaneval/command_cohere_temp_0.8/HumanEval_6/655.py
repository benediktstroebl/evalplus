```python
from typing import List

def parse_nested_parens(s: str) -> List[int]:
    result = []
    for i, char in enumerate(s.split()):
        nested = 0
        level = 0
        j = 0
        while j < len(char):
            if char[j] == '(':
                nested += 1
                level = max(level, nested)
            elif char[j] == ')':
                nested -= 1
            j += 1
        result.append(level)
    return result
```

The provided Python script solves the problem of parsing nested parentheses and returns the deepest level of nesting for each group in the input string separated by spaces.

The function takes a string as input and uses a loop to split the input string into characters and determine the deepest level of nesting of parentheses for each character sequence. The maximum nested level is tracked using the `level` variable and updated accordingly as the loop iterates through each opening and closing parenthesis. The function returns a list of the deepest nesting levels for each group.