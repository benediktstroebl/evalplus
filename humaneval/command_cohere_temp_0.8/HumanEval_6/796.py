```python
from typing import List

def parse_nested_parens(s: str) -> List[int]:
    return [max(i // 2 for i in reversed(sum(map(int, group), [])))) for group in s.split()]
```

The provided Python script demonstrates a function called `parse_nested_parens`, which takes a string (`s`) as input and returns a list of integer values. This function is designed to solve the problem of computing the deepest level of nesting of parentheses in a given string that contains multiple groups of nested parentheses separated by spaces.

The function uses a combination of integer conversion, summing, and maximum value extraction to determine the maximum depth of nesting for each group of parentheses. It achieves this by converting each group into an integer value, summing these values to obtain a single integer, and then taking the maximum depth of nesting as the highest value divided by 2 (since nesting depth is even).

The function is self-contained, meaning it does not rely on external variables or modules. It uses the `typing` module to declare the input parameter as a string and the return value as a list of integers. The function is designed to be robust and compatible with different versions of Python, ensuring easy adoption and usage in various environments.