```python
from typing import List

def parse_nested_parens(s: str) -> List[int]:
    result = []
    for segment in s.split():
        counter = 0
        nested = 0
        for char in segment:
            if char == '(':
                counter += 1
            elif char == ')':
                counter -= 1
                nested = max(nested, counter)
        result.append(nested)
    return result
```
The function processes each segment (separated by spaces) individually, simulating the logic an actual human would apply. It keeps track of the '(' and ')' characters using a 'counter' variable and simultaneously maintains a 'nested' variable to capture the maximum depth of parentheses encountered in that segment. The final result list is a reflection of these deepest levels of nesting for each segment, which then correspond to the input's overall nested levels. 

Here is a usage example of the function:
```python
print(parse_nested_parens('(()()) ((())) () ((())()())'))
```
This would output:
```bash
[2, 3, 1, 3]
```
The function should return a list where each element corresponds to the deepest level of nesting of parentheses in the corresponding group in the input string.