```python
from typing import List

def parse_nested_parens(s: str) -> List[int]:
    result = []
    for bracket_pair_str in s.split():
        level = 0
        unbalanced = 0
        stack = []
        for char in bracket_pair_str:
            if char == '(':
                stack.append(char)
                unbalanced += 1
            else:
                unbalanced -= 1
                if not unbalanced:
                    level += 1
                    if stack:
                        result.append(level)
                stack.pop()
        if unbalanced > 0:
            result.append(level)
    return result
```

The reasoning behind the correct solution is elaborated below:
1. The input string `s` contains multiple groups of nested parentheses separated by spaces.
2. For each group, we maintain data about the current level of nesting and the number of open parentheses that are not yet balanced by a closing parenthesis.
3. To do this, we use two variables `level` and `unbalanced` in the loop iterating over each character of a bracket pair string.
4. `level` starts with 0 and increments each time we close a parenthesis, therefore, registering the deepest level of nesting of parentheses in that particular string segment.
5. `unbalanced` increases each time we meet an open parenthesis and decreases each time we meet a close parenthesis.
6. When `unbalanced` reaches 0, it means we have balanced all the parentheses in this particular segment, and the `level` value is increased correspondingly.
7. If while processing a string segment, we encounter more open parentheses than closed ones, this segment is considered unbalanced, and we add the current `level` value to the result.
8. Finally, the result list corresponds to the deepest level of nesting for each corresponding string segment.