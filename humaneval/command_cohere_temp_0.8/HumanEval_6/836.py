```python
from typing import List

def parse_nested_parens(s: str) -> List[int]:
    result = []
    for i, char in enumerate(s.replace(' ', '')):
        if char == '(':
            nest = 1
            j = i
            while j < len(s) and nest != 0:
                if s[j] == '(':
                    nest += 1
                elif s[j] == ')':
                    nest -= 1
                j += 1
            result.append(nest)
        elif char == ')':
            result.append(0)
    return result
```

The nested level is captured through a pointer (`nest`) that increments inside parentheses and decrements outside them. The loop iterates through each character and adjusts the pointer accordingly. When encountering a closing parenthesis, the `nest` value is recorded as zero in the result list.

The problem is tested using the provided Markdown code block containing example inputs and expected outputs. To run the test, copy the code into a Python file, execute it, and verify that the output matches the expected results.