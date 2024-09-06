```python
from typing import List

def parse_nested_parens(s: str) -> List[int]:
    result = []
    for segment in s.split():
        depth = 0
        imbalance = 0
        i = 0
        for char in segment:
            if char == '(':
                depth += 1
                imbalance += 1
            elif char == ')':
                depth -= 1
                imbalance -= 1
            if imbalance > 0:
                result.append(depth)
                i += 1
                imbalance = 0
        if imbalance > 0:
            result.append(depth)
            i += 1
        # this condition ensures we stop running the algorithm when we hit a unbalanced string with no parentheses
        if i == len(segment):
            result.append(0)
    return result
```

The logic is straightforward. We iterate over each character in the string and whenever we hit a '(', we increase the depth and maintain a separate variable called imbalance which keeps track of extra '(' count. Whenever we encounter a ')', we decrease the depth and reduce the imbalance by 1. Now, the imbalance value gives us the number of extra '(' we have, so we keep adding the depth to the result array and incrementing the index until we reach a balanced state where imbalance becomes 0. We also add a check to make sure we stop running the algorithm if we hit an unbalanced string end without encountering a closing parentheses. The overall time complexity is O(N) where N is the length of the string.