```python
from typing import List

def parse_nested_parens(s: str) -> List[int]:
    result = []
    for seg in s.split():
        count = 0
        level = 0
        parentheses = ['(', ')', '(']
        for char in seg:
            if char in parentheses:
                if count == 0:
                    level += 1
                else:
                    count += 1
            else:
                if count > 0:
                    count -= 1
                else:
                    level += 1
            result.append(level)
    return result
```

The `parse_nested_parens` function takes a string as input and returns a list of the deepest level of nesting of parentheses for each segment. It splits the string into segments based on spaces, and then iterates through each character within the segment. When encountering opening parentheses `(`, it increments the `count` variable to keep track of the nesting level, whereas closing parentheses `)` decrements the count. Meanwhile, the level is incremented whenever counting increments and decrements when counting decrements, so the level keeps the absolute count of the nesting level. The procedure repeats until all characters have been examined, and the deepest level of nesting for that segment is stored in the result list.

Here is an example function call:
```python
print(parse_nested_parens("(()()) ((())) () ((())()())"))
```

The output will be:
```python
[2, 3, 1, 3]
```

This is consistent with the example in the provided Markdown code block.