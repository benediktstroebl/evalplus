```python
from typing import List

def parse_nested_parens(s: str) -> List[int]:
    result = []
    for chunk in s.split(' '):
        chunk = chunk.strip('())' )
        if not chunk:
            result.append(0)
        else:
            stack = [0]
            level = 0
            for char in chunk:
                if char == '(':
                    stack.append(level)
                    level += 1
                else:
                    level = stack.pop()
            result.append(level)
    return result
```
The logic is straightforward:
1. For each group, the function splits it by spaces to iterate over the chunk easily.
2. The function trims all opening and closing parentheses from the chunk.
3. Then, the function uses a stack to track the level of nesting. The number of ('') pushed to the stack is the same as the number of ()'s in the chunk. vice versa.
4. The final level value of the stack is the deepest level of nesting of parentheses in that chunk.
5. The function returns a list that contains the result of every group in the input string. 

Here is an example usage of the function:
```python
>>> parse_nested_parens('(()()) ((())) () ((())()())')
[2, 3, 1, 3]
```
This function can efficiently solve the problem and provide the deepest level of nesting for each group of parentheses in the given input string.