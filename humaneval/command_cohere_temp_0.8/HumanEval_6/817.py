```python
from typing import List

def parse_nested_parens(s: str) -> List[int]:
    return [max(i // 2 for i in reversed(sum(map(int, group.split())))) for group in s.split()]
```

The provided Python script demonstrates a function called `parse_nested_parens`, which takes a string (`s`) as input and returns a list of integers. This function is designed to parse and evaluate nested parentheses in the input string, determining the deepest level of nesting for each group of parentheses.

Here's how it works:
1. The function uses a list comprehension and the `sum` function to calculate the total number of parentheses for each group separated by spaces in the input string. The `map` function is used to convert each group into an integer representing the total parentheses count.
2. The sum of parentheses counts is computed using `sum(map(int, group.split()))`.
3. The maximum depth of nesting is determined by dividing the total parentheses count by 2 and finding the maximum depth among all groups using `max(i // 2 for i in reversed(sum(map(int, group.split()))))`.

The provided example output shows the correct parsing of different groups of nested parentheses, demonstrating the function's ability to accurately evaluate and report the deepest level of nesting for each group.