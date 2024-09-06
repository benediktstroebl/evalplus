```python
from typing import List

def parse_nested_parens(s: str) -> List[int]:
    result = []
    for chunk in s.split():
        counter = 0
        for char in chunk:
            if char == '(':
                counter += 1
            else:
                counter -= 1
        result.append(counter)
    return result
```
The logic behind this approach is straightforward. We iterate over each character in a chunk and maintain a counter that keeps track of the imbalance of open parentheses '(' minus closed parentheses ')' we encounter. This counter directly gives us the maximum depth of nesting of parentheses in that particular chunk. Then we iterate over each chunk in the input string, splitting it via space, and keep track of the deepest level of nesting for each group, storing them in the result list. 

This approach has a time complexity of O(n), where n is the size of the input string, as it requires parsing each character in the string once.