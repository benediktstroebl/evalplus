```python
from typing import List

def parse_nested_parens(s: str) -> List[int]:
    result = []
    for segment in s.split():
        nest = 0
        imbalance = 0
        for char in segment:
            if char == '(':
                nest += 1
                imbalance += 1
            elif char == ')':
                nest -= 1
                imbalance -= 1
            if imbalance > 0:
                result.append(nest)
                imbalance = 0
    return result
```

This Python script includes a self-contained function `parse_nested_parens` that takes a string `s` containing multiple groups of nested parentheses separated by spaces, as provided in the prompt. It processes each segment (a substring surrounded by spaces) individually, keeping track of the current nesting level (`nest`) and imbalance (number of open parentheses minus closed parentheses). 

For each character in a segment, it increments or decrements the nesting level based on whether the character is an open or closed parenthesis. If the imbalance is positive (open parentheses excess), it appends the current nesting level to the results list and resets the imbalance to 0, as starting a new segment. Finally, it returns a list of maximum nesting levels for each segment, which represents the deepest level of nesting of parentheses in each group.