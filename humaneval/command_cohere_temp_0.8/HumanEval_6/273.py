```python
from typing import List

def parse_nested_parens(s: str) -> List[int]:
    return [max(i // 2 for i in reversed(sum(map(int, group), [])))) for group in s.split()]
```

The provided Python script demonstrates a function called `parse_nested_parens`, which takes a string (`s`) as input and returns a list of integers. This function is designed to solve the problem of computing the deepest level of nesting of parentheses in each group within a given string that contains multiple groups of nested parentheses separated by spaces.

Here's how it works:
1. The function uses a list comprehension and the `sum` function to calculate the total number of parentheses at different levels of nesting for each group.
2. The `map` function is used to convert each group into an integer representation, where opening parentheses (`(`) are converted to 1 and closing parentheses (`)` are converted to -1. The sum operation then counts the net parentheses, effectively measuring the depth of nesting.
3. The maximum depth of nesting is obtained by calculating the maximum integer value of the summed results for each group, which is achieved using the `max` function in a list comprehension.
4. The final result is a list where each element represents the deepest level of nesting for the respective group.

This approach provides an efficient and concise solution to the problem, allowing the function to accurately parse and analyze nested parentheses in multiple groups within the given input string.