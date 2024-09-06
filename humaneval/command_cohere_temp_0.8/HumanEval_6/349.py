```python
from typing import List

def parse_nested_parens(s: str) -> List[int]:
    result = []
    for chunk in s.split(' '):
        level = 0
        curr = 0
        for c in chunk:
            if c == '(':
                curr += 1
            elif c == ')':
                curr -= 1
            else:
                pass
            level = max(level, curr)
        result.append(level)
    return result
```
The `parse_nested_parens` function takes a string as input and returns a list of the deepest levels of nesting of parentheses in each sub-string. It operates as follows:
1. It splits the input string into space-separated chunks, which represent different groups of parentheses. 
2. For each chunk, it initializes a level counter at 0, which keeps track of the maximum depth of parentheses encountered. It also initializes an open parentheses counter at 0.
3. It iterates through each character in the chunk. If the character is an open parentheses '(', it increments the open parentheses counter. If it's a closing parentheses ')', it decrements the counter. Otherwise, it skips non-parentheses characters.
4. The maximum depth of parentheses is the maximum of the current counter value and the current counter value minus one. This is because when we iterate through the string, we care about the deepest level of nesting. For example, both ('()(())' and '((()))' have a maximum depth of 2.
5. After processing each chunk, it updates the result list with the maximum depth of parentheses for that chunk.
6. Finally, it returns the list of maximum depths for each chunk.