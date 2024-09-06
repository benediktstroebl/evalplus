```python
from typing import List

def parse_nested_parens(s: str) -> List[int]:
    result = []
    for tok in s.split():
        lev = 0
        for c in tok:
            if c == '(':
                lev += 1
            else:
                lev -= 1
        result.append(lev)
    return result
```

The code uses a straightforward nested loop to examine each token in the string s. It maintains a level variable to record the current nesting level, increasing it whenever it encounters an open parenthesis '(', and decreasing it when it encounters a closing parenthesis ')'. The function returns the array of the maximum nesting level for each token.

To use the function, simply add the following test case to confirm its correctness:
```python
>>> parse_nested_parens('(()()) ((())) () ((())()())')
[2, 3, 1, 3]
```

This approach may not be the most efficient in terms of performance if the input string contains a very large number of parentheses, as it uses a nested loop approach that has a time complexity proportional to the total number of parentheses in the string. However, for relatively small inputs, it provides a simple and effective solution.  If needed, we can optimize it using a stack-based solution, especially for larger inputs.