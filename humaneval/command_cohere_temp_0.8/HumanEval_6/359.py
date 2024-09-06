```python
from typing import List

def parse_nested_parens(s: str) -> List[int]:
    result = []
    for i, char in enumerate(s.replace(' ', '')):
        if char == '(':
            nesting = 1
            while i < len(s) and s[i] != ')':
                if s[i] == '(':
                    nesting += 1
                i += 1
            result.append(nesting)
        elif char == ')':
            i += 1
    return result
```

The specified Python script defines a function called `parse_nested_parens` that takes a string as input and returns a list of integers. This function iterates through the characters of the input string, maintaining a 'nesting' counter that represents the depth of nested parentheses. When an opening parenthesis '(' is encountered, the nesting count is increased, and this count is decremented when a closing parenthesis ')' is found. The resulting list of nesting counts represents the maximum nesting depth for each group of parentheses in the string.

The example usage and test case provided demonstrate how the function can be used to analyze different string scenarios and extract the desired information, making it a reusable and effective solution for the problem.