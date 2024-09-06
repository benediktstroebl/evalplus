```python
from typing import List

def parse_nested_parens(s: str) -> List[int]:
    result = []
    for i, char in enumerate(s.replace(' ', '')):
        if char == '(':
            nesting = 1
            while i < len(s) and nesting > 0:
                if s[i] == '(':
                    nesting += 1
                elif s[i] == ')':
                    nesting -= 1
                i += 1
            result.append(nesting)
    return result
```

The provided Python script defines a function called `parse_nested_parens` that takes a string as input and returns a list of deepest levels of nesting of parentheses in each group separated by spaces. 

The script is self-contained and can be executed independently. It does not rely on any external dependencies or modules other than the standard Python library.

To validate the functionality of the script, it is recommended to incorporate tests, as shown in the original problem statement. These tests can encompass various scenarios of nested parentheses to ensure the accuracy of the function's behavior.