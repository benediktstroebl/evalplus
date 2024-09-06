```python
from typing import List

def parse_nested_parens(s: str) -> List[int]:
    result = []
    for chunk in s.split():
        count = 0
        nested = 0
        non_nested = 0
        for char in chunk:
            if char == '(':
                nested += 1
            elif char == ')':
                nested -= 1
                non_nested += 1
            count = max(count, nested)
        result.append(count)
    return result
```

The code splits the input string into spaces and then processes each chunk to count the '(' and ')' to determine the maximum nested level. The maximum nested level is stored in the result list that is returned after processing all chunks. 

Here is an example output of the function:
```python
parse_nested_parens('(()()) ((())) () ((())()())')
[2, 3, 1, 3]
``` 

This is the expected output as the string contains nested parentheses of different lengths and the function will return a list of depths of each group of parentheses.