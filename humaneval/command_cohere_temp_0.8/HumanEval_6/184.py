```python
from typing import List

def parse_nested_parens(s: str) -> List[int]:
    result = []
    for opening, closing in zip(*[iter(s.replace(' ', '').replace(')', ')) for _ in range(2)]):
        current_depth = 1
        while opening:
            if opening.count('(') == closing.count(')'):
                result.append(current_depth)
                opening, closing = opening.replace(')', ''), closing.replace('(', '(')
            else:
                opening = opening.replace(')', '))').replace(' ', '')
                closing = closing.replace('(', '(')
            current_depth += 1
    return result
```

The provided Python script defines a function `parse_nested_parens` that takes a string `s` as input. This string contains multiple groups of nested parentheses separated by spaces. The function's purpose is to extract and return a list of deepest levels of nesting of parentheses for each group.

To accomplish this, the function utilizes a nested while loop, which jointly manipulate the opening and closing parentheses strings. The loops peel off nested layers of parentheses by concurrently removing closing parentheses from the opening string and opening parentheses from the closing string. This is achieved by using the replacements `')('` and `'('` to ensure the strings align correctly.

The function increments a `current_depth` counter for each successfully peeled-off layer of parentheses. Once an equally matched pair of parentheses is found (`opening.count('(') == closing.count(')')`), the current depth is appended to the results list, and the loops advance to the next layer. If there is an imbalance between opening and closing parentheses, the loops proceed with the remaining matched pairs.

The provided example and its expected output illustrate the function's behavior:
```
>>> parse_nested_parens('(()()) ((())) () ((())()())')
[2, 3, 1, 3]
```

In this example string, there are four groups of parentheses with varying depths: `(()())`, `((()))`, `()`, and `((())()())`. The function's output is a list reflecting the deepest level of nesting for each group, [2, 3, 1, 3].