```python
from typing import List

def parse_nested_parens(s: str) -> List[int]:
    result = []
    for token in s.split():
        balance = 0
        i = 0
        for char in token:
            if char == '(':
                balance += 1
            else:
                balance -= 1
            i += 1
        result.append(balance)
    return result
```

The reasoning behind the correct solution is Thinking about the problem, we realize that to get the maximum depth of nesting, we should track the balance of open and closed parentheses. Every time we encounter an open parenthesis, we increase the balance, and every time we encounter a closed parenthesis, we decrease the balance. The maximum depth of nesting is reached when we encounter a closed parenthesis and the balance becomes zero. Therefore we can simply iterate over the string and keep track of the balance to find the maximum depth of nesting for each group.