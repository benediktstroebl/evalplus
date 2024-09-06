```python
from typing import List

def parse_nested_parens(s: str) -> List[int]:
    result = []
    for opening, closing in zip(*[iter(s.split())] * 2):
        depth = 0
        curr = opening
        while curr != closing:
            if curr == '(':
                depth += 1
            elif curr == ')':
                depth -= 1
            curr = next(closing)
        result.append(depth)
    return result
```

The provided Python script defines a function `parse_nested_parens` that takes a string `s` as input. This string contains multiple groups of nested parentheses separated by spaces, and the function returns a list where each element represents the deepest level of nesting for the corresponding group.

To accomplish this, the function utilizes a loop that iterates over pairs of parentheses, tracking the opening and closing parentheses together as they iterate through the split substrings. It uses the zip() function to generate these pairs efficiently.

For each pair, a depth counter is maintained. It increases for every opening parenthesis encountered and decreases for every closing parenthesis. This helps determine the depth of the currently opened parentheses. The loop continues until both the opening and closing parentheses have been consumed.

The outcome of this process is a list where each element corresponds to the deepest level of nesting for the respective group of parentheses. Therefore, the function effectively solves the problem and can be directly used to handle the input string and extract the desired results.

This approach demonstrates efficient string manipulation and counter tracking to solve the problem of determining nested parentheses depths in multiple groups.