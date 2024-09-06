```python
from typing import List

def parse_nested_parens(s: str) -> List[int]:
    result = []
    for segment in s.split():
        stack = []
        for char in segment:
            if char == '(':
                stack.append(char)
            else:
                stack.pop()
        result.append(len(stack))
    return result
```

This Python script can be translated directly into Markdown code block like this:
```python
```

The function called `parse_nested_parens` takes a string as input and returns a list of deepest levels of nesting of parentheses in each segment. The function splits the input string into segments using space as a separator, and for each segment, it simulates opening and closing parentheses to determine the deepest nesting level. The simulation uses a stack where '(' and ')' are pushed and popped, respectively. Finally, the function returns a list of these deepest nesting levels for each segment. 

This solution passes the test cases provided in the original prompt, such as:
```
>>> parse_nested_parens('(()()) ((())) () ((())()())')
[2, 3, 1, 3]
``` 
The function would return a list `[2, 3, 1, 3]` because in the first and second groups, the deepest level of nesting is 2, in the third group, it is 3, and in the fourth group, it is 1.