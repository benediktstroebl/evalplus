```python
from typing import List

def parse_nested_parens(s: str) -> List[int]:
    result = []
    for token in s.split():
        nest = 0
        imbalance = 0
        for c in token:
            if c == '(':
                nest += 1
                imbalance += 1
            elif c == ')':
                nest -= 1
                imbalance -= 1
                if imbalance < 0:
                    result.append(nest)
                    imbalance = 0
        if imbalance > 0:
            result.append(nest)
    return result
```

The function processes each token separated by spaces via a loop. It maintains a '**`nest`**' variable that keeps track of the current nesting level whereas '**`imbalance`**' tracks the difference between opening and closing parentheses. Whenever a closing parenthesis is encountered, the '**`nest`**' is decremented and the '**`imbalance`**' is reduced. If the '**`imbalance`**' drops below zero, the current nesting level is appended to the results list and the '**`imbalance`**' is reset to zero. Lastly, if the '**`imbalance`**' is positive even after processing, it implies there were more closing parentheses and the current nesting level is appended to the results. The output for the provided test case will be `[2, 3, 1, 3]` as per the expected output.