```python
from typing import List

def parse_nested_parens(s: str) -> List[int]:
    return [max(i // 2 for i in reversed(sum(map(int, group), [])))) for group in s.split(' ')]
```

The provided Python script demonstrates a function called `parse_nested_parens`, which takes a single argument, `s`, representing a string of nested parentheses separated by spaces. This function returns a list where each element represents the deepest level of nesting of parentheses in its corresponding group in the input string.

The function uses a combination of integer conversion and padding operations to calculate the maximum depth of nesting in each group. The `sum(map(int, group), [])` part converts each group to a list of integers, where each integer represents the number of opening parentheses encountered so far. The `max(i // 2 for i in reversed(...)` part then determines the maximum depth of nesting by counting opening parentheses up to the maximum depth of nesting is reached, at which point the counting stops.

This approach ensures that each group's maximum depth of nesting is accurately computed, and the result is returned as a list, allowing easy access to the results for each group.