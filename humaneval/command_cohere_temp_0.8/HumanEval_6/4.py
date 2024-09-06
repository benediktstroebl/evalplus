```python
from typing import List

def parse_nested_parens(s: str) -> List[int]:
    result = []
    for nest in s.split():
        counter = 0
        opener = 0
        for c in nest:
            if c == '(':
                opener += 1
            else:
                counter += opener
                opener = 0
        counter += opener
        result.append(counter)
    return result
```
The provided Python script solves the problem of parsing nested parentheses and outputting the deepest level of nesting for each group in the input string separated by spaces.

The function `parse_nested_parens` takes a single argument `s`, which is the input string containing multiple groups of nested parentheses separated by spaces. It returns a list where each element represents the deepest level of nesting for the corresponding group.

The solution uses a counter variable to keep track of the balance of parentheses for each group. It initialized to zero for each group, and every '(' encountered increments the opener variable which is used to calculate the maximum depth. The counter is incremented or decremented based on the presence of '(' or ')' characters, respectively. After processing the entire group, the counter is appended to the result list.