```python
from typing import List

def parse_nested_parens(s: str) -> List[int]:
    result = []
    for token in s.split():
        stack = []
        depth = 0
        for char in token:
            if char == '(':
                stack.append(depth)
                depth += 1
            else:
                depth = stack.pop()
        result.append(depth)
    return result
```

The provided Python script demonstrates a function called `parse_nested_parens`, which takes a string (`s`) as input and returns a list of integer values. This function is designed to solve the problem of computing the deepest level of nesting of parentheses for each group in a given string that represents multiple groups of nested parentheses separated by spaces.

Here's how the function works:
1. The given input string is split into individual tokens using the `split()` method, where each token represents a group of parentheses.
2. For each token, the function initializes a stack (represented as an integer list) and a variable `depth` to keep track of the current depth of nesting.
3. As the function iterates through each character of the token, it performs the following steps:
   - If the character is `'('` (open parenthesis), it pushes the current depth `depth` into the stack and increments `depth` by 1 to represent the increase in nesting level.
   - If the character is `')'` (close parenthesis), it pops the top value from the stack, which represents the starting depth of the nested parentheses, and assigns it to `depth`. The `depth` value is then incremented by 1 to account for the closing parenthesis.
4. The function continues this process for each character in the token, keeping track of the maximum depth of nesting achieved.
5. After processing all tokens, the function returns a list of the deepest levels of nesting for each group of parentheses.

This code will correctly solve the problem of calculating the maximum nesting level for each group of parentheses in the provided input string.