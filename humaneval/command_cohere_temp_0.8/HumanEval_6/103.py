```python
from typing import List

def parse_nested_parens(s: str) -> List[int]:
    return [max(i // 2 for i in reversed(sum(map(lambda x: list(zip(x, x[1:])), ('(' + subs + ')').split()))))
            for subs in s.split(' ')]
```

The provided Python script defines a function called `parse_nested_parens` that takes a string input `s`, representing multiple groups for nested parentheses separated by spaces. This function's purpose is to calculate and return a list of deepest levels of nesting of parentheses for each group.

The function utilizes a generator expression within a list comprehension to determine the maximum depth of nesting for each substring bracketed by parentheses within the given string. It does this by utilizing a counter `i` that tracks the number of closing parentheses ')' encountered while iterating through each substring. The maximum depth of nesting is determined by calculating the maximum value of `i // 2` across all substrings.

To handle multiple groups of parentheses separated by spaces, the function iterates over each substring, unties the substrings, and calculates their nesting depths. The resulting list of depths is then returned.

This solution is self-contained, meaning it does not rely on external variables or functions, and it can be safely executed independently for testing and verification.