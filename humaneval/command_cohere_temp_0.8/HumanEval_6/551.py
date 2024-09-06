```python
from typing import List

def parse_nested_parens(s: str) -> List[int]:
    result = []
    for chunk in s.split(' '):
        nesting = 0
        level = 0
        for c in chunk:
            if c == '(':
                nesting += 1
                level = max(level, nesting)
            elif c == ')':
                nesting -= 1
        result.append(level)
    return result
```

The `parse_nested_parens` function takes a string as input and returns a list of the deepest nesting level of parentheses in each sub-string. It operates as follows:
1. It splits the input string into space-separated chunks. Each chunk represents a group of parentheses that might have different depths of nesting.
2. For each chunk, it initializes `nesting` and `level` variables. The `nesting` variable counts the current nesting level, and the `level` keeps track of the maximum nesting level encountered so far.
3. As it iterates through each character of the chunk, it adjusts the `nesting` level accordingly: 
    - If the character is `(`, it increments `nesting` and updates `level` with the maximum value between the current `nesting` and `level`. This ensures that if a new nested layer is encountered, the `level` is updated to reflect that new maximum. 
    - If the character is `)`, it decrements the `nesting`. 
4. Finally, when all characters have been processed, it appends the `level` to the `result` list, which is returned. 

The provided example and test cases are correct, and the function should handle any string of parentheses, including unbalanced ones. If the input string is `(())`, the expected result is `[2]`, and if the input is `((()))`, the expected result is `[3]`.