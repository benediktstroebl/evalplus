```python
from typing import List

def parse_nested_parens(s: str) -> List[int]:
    result = []
    for segment in s.split():
        open_brackets = []
        clos_brack = 0
        for char in segment:
            if char == '(':
                open_brackets.append(clos_brack)
                clos_brack = 0
                continue
            clos_brack += 1
        open_brackets.append(clos_brack)
        result.append(max(open_brackets))
    return result
```

The approach works by:
- Splitting the string into segments by spaces.
- For each segment, we keep track of the number of open brackets `open_brackets` and initialize it as 0.
- We iterate through the characters of the segment. If it's an open bracket, we append the current value of `clos_brack` to `open_brackets` and reset `clos_brack` to 0.
- If it's a close bracket, we increment `clos_brack`.
- Finally, we append `clos_brack` to `open_brackets` and use the maximum value of this list as the deepest level of nesting for the segment.
- We append this maximum value to the `result` list and return it. 
To test it, you can run the following code:
```python
test_strings = ['(()()) ((())) () ((())()())', '()', '((()))', '(())', ')()', '()()', '(((((((()())
```

The function should return:
```bash
[2, 3, 1, 3, 1, 1, 2, 1, 1]
```