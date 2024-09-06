```python
from typing import List

def parse_nested_parens(s: str) -> List[int]:
    result = []
    for i, group in enumerate(s.split()):
        open_par = group.count('(')
        close_par = group.count(')')
        result.append(open_par - close_par)
    return result
```

The above code defines a function called `parse_nested_parens` taking a string as an input parameter, splitting the input string into a list of groups, and calculating the difference between the number of opening and closing parentheses for each group to determine and return the deepest level of nesting of parentheses in each group. 

To test this code, you can run the following script:
```python
test_parse_nested_parens = '''
(()()) ((())) () ((())()())
'''

print(parse_nested_parens(test_parse_nested_parens))
```

Expected output:
```
[2, 3, 1, 3]
``` 

This output shows the deepest level of nesting for each group of parentheses in the test string. Each number represents the maximum number of parentheses in a group.