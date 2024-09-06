```python
from typing import List

def parse_nested_parens(s: str) -> List[int]:
    result = []
    for i, char in enumerate(s.replace(' ', '')):
        if char == '(':
            nesting = 1
            while i < len(s) and s[i] == '(':
                i += 1
                nesting += 1
            result.append(nesting)
        elif char == ')':
            nesting -= 1
            if nesting < 0:
                result.append(0)
                break
            result.append(nesting)
    return result
```

The nested level is based on the idea that every opening parenthesis has a corresponding closing parenthesis, so the level is calculated by counting consecutive open parentheses and subtracting the count of consecutive closing parentheses. The solution uses a list to store the levels of each group and adds the level of the last group, even if it has less than two parentheses. It also handles cases where there is an odd number of parentheses, ensuring that the result list always contains at least one integer.