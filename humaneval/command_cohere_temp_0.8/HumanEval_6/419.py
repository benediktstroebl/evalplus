```python
from typing import List

def parse_nested_parens(s: str) -> List[int]:
    result = []
    for i, char in enumerate(s.replace(' ', '')):
        if char == '(':
            nesting = 1
            while i < len(s) and s[i] == '(':
                i += 1
                nesting += 1
            result.append(nesting)
        elif char == ')':
            nesting -= 1
            if nesting < 0:
                result.append(nesting)
                break
    return result
```

The specified Python script defines a function called `parse_nested_parens` that takes a string as input and returns a list of deepest levels of nesting of parentheses in each group separated by spaces. 

For each group, the function counts the number of opening parentheses '(' and subtracts the number of closing parentheses ')' from it. It keeps doing this until it reaches the deepest level of nesting for that group. The function then adds the deepest level of nesting for each group to the `result` list and breaks out of the loop to move on to the next group. The resulting list is then returned.