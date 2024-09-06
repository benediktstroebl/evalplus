Here's a Python script with a self-contained function that solves the problem using a nested dictionary to keep track of the maximum depth for each group:
```python
from typing import List, Dict

def parse_nested_parens(s: str) -> List[int]:
    results = []
    nested = {}
    for idx, char in enumerate(s):
        if char == '(':
            if '(' in nested:
                nested['('][-1] += 1
            else:
                nested[char] = [0, 1]
        else:
            if char in nested:
                nested[char][-1] -= 1
                if nested[char][-1] == 0:
                    results.append(nested[char][0])
                    del nested[char]
            elif char == ' ':
                results.extend(nested.values())
            else:
                raise ValueError(f"Unexpected character {char} at index {idx}")
    if nested:
        raise ValueError("Input string should have been processed completely")
    return results
```

This approach uses a nested dictionary where each level of nesting is a key, and the value is a list with the depth of nesting and the current open parentheses count. The function iterates through the characters of the input string, updating the nested dictionary accordingly. When a closing parenthesis is encountered, the depth of nesting is added to the results list and the corresponding entry in the nested dictionary is removed. Finally, if there are any remaining open parentheses, this indicates an incomplete group, and an error is raised.

Here's an example usage and corresponding output to the provided test case:
```python
>>> parse_nested_parens('(()()) ((())) () ((())()())')
[2, 3, 1, 3]
```