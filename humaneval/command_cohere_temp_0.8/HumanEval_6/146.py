```python
from typing import List

def parse_nested_parens(s: str) -> List[int]:
    result = []
    for chunk in s.split():
        count = 0
        nesting = 0
        for char in chunk:
            if char == '(':
                nesting += 1
            else:
                nesting -= 1
            count = max(count, nesting)
        result.append(count)
    return result
```

The `parse_nested_parens` function takes a string as input and returns a list of the maximum depth of parentheses nesting for each corresponding chunk of the string. It performs the following steps:
1. It splits the input string `s` into chunks using spaces as separators.
2. For each chunk, it initializes a variable `count` to keep track of the maximum depth of parentheses nesting encountered. It also initializes `nesting` to keep track of the current nesting level.
3. It iterates through each character in the chunk. If the character is `'('` (open parentheses), it increments the `nesting` level. If the character is `')'` (close parentheses), it decrements the `nesting` level.
4. During each iteration, it updates the `count` with the maximum value between the current `nesting` level and the previous `count`. This ensures that `count` always holds the maximum depth of parentheses nesting for the entire chunk.
5. Finally, it appends the calculated `count` to the `result` list, which accumulates the deepest level of nesting for each chunk.

The script passes the provided test case and produces the expected output. 
```python
>>> parse_nested_parens('(()()) ((())) () ((())()())')
[2, 3, 1, 3]
``` 
It effectively captures the maximum depth of parentheses nesting for each separate group of parentheses in the provided string.