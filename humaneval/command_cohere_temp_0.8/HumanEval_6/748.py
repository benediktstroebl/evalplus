```python
from typing import List

def parse_nested_parens(s: str) -> List[int]:
    result = []
    for i, char in enumerate(s.replace(' ', '')):
        if char == '(':
            nest = 1
            j = i
            while nest > 0:
                j += 1
                if s[j] == '(':
                    nest += 1
                elif s[j] == ')':
                    nest -= 1
            result.append(j - i)
        elif char == ')':
            result.append(0)
    return result
```

The algorithm works by:
1. Taking an input string and removing all spaces to make the problem more straightforward and dealing with nested parentheses only.
2. Using a loop to iterate through characters in the string.
3. Whenever we encounter an open parentheses `(`, we do the following
    - Increment a counter `nest` which keeps track of the nesting level.
    - Use a variable `j` to track the ending parentheses `)` to calculate the deepest level by incrementing it in the case of a parenthesis and decrementing it in the case of a closing parenthesis.
4. Once we encounter a closing parenthesis), we reset the counter to 0 as we start considering the next group of parentheses.
5. Finally, return a list of deepest levels of nesting for all groups of parentheses.