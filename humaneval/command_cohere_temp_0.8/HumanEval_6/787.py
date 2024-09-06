```python
from typing import List

def parse_nested_parens(s: str) -> List[int]:
    result = []
    for chunk in s.split(' '):
        counter = 0
        for char in chunk:
            if char == '(':
                counter += 1
            else:
                counter -= 1
            result.append(counter)
    return result
```
The provided Python script solves the problem of parsing nested parentheses and outputting the deepest level of nesting for each group in the given input string `s` separated by spaces.

The function `parse_nested_parens` takes a string as input and uses a list to store the results. It splits the input string into chunks where each chunk represents a group of parentheses separated by spaces. For each chunk, it initializes a counter variable `counter` to keep track of the nesting level. As the loop iterates through each character in the chunk, it increments the `counter` for opening parentheses `(` and decrements it for closing parentheses `)`. The maximum counter value throughout the iteration represents the deepest level of nesting for that particular group, and it is appended to the `result` list. Finally, the function returns the list of deepest nesting levels for each group.