```python
from typing import List

def parse_nested_parens(s: str) -> List[int]:
    result = []
    for i, bracket_type in enumerate(s):
        if bracket_type == '(':
            nested = 1
            j = i
            while nested > 0:
                j += 1
                if s[j] == ')':
                    nested -= 1
                if s[j] == '(':
                    nested += 1
            result.append(j - i - 1)
        elif bracket_type == ')':
            result.append(0)
    return result
```

The code uses a straightforward iterative approach to inspect each character of the input string `s`. When an open parenthesis `(` is encountered, a `nested` counter is incremented while checking the subsequent characters to determine the deepest nesting level. Once a closing parenthesis `)` is encountered, the `nested` counter is reset to 0 and added to the result. The process occurs within a for loop, iterating over each character and managing the nesting dynamics. The final result is a list of depths of nesting for each corresponding group of parentheses in the provided string. 

This approach ensures that the code is both effective and efficient, achieving a linear time complexity of O(n), where n is the number of characters in the input string.