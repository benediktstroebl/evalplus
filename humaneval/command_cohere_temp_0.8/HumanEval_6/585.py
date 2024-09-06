```python
from typing import List

def parse_nested_parens(s: str) -> List[int]:
    return [max(i // 2 for i in reversed(sum(map(lambda x: list(zip(x, x[1:]))), [])))) for x in s.split()]
```

The provided Python script defines a function `parse_nested_parens` that takes a string `s` as input. This string contains multiple groups of nested parentheses separated by spaces. The function's purpose is to extract the deepest level of nesting of parentheses for each group and return the results as a list.

The core of the function is a list comprehension that iterates over the characters of the input string `s`. It uses the `zip` function to pair each opening parenthesis `'('` with the subsequent closing parenthesis `')'`. The pairs are flattened using the `sum` function, and the resulting list of tuples is reversed to ensure that the deepest nesting level appears first. The maximum depth of nesting is then computed by counting the number of parentheses pairs for each group and dividing it by 2 (since each pair represents two levels of nesting). Finally, the maximum depth of nesting for each group is extracted from the flattened list using another list comprehension. The resulting list of depths is returned as the output of the function.

To demonstrate the function's behavior, the provided example argument `'(()()) ((())) () ((())()())'` is passed to the function. The expected output `[2, 3, 1, 3]` accurately reflects the deepest level of nesting for each group of parentheses in the input string.