```python
from typing import List

def parse_nested_parens(s: str) -> List[int]:
    result = []
    for chunk in s.split(' '):
        nest = 0
        level = 0
        for char in chunk:
            if char == '(':
                nest += 1
                level = max(level, nest)
            else:
                nest -= 1
        result.append(level)
    return result
```

The `parse_nested_parens` function takes a string as input and splits it into chunks using spaces as separators. It then iterates over each character in each chunk, maintaining a counter for the current nesting level `nest` and updating it accordingly when it encounters '(' or ')' characters. The maximum nesting level `level` encountered within each chunk is recorded in the `result` list.

To verify the functionality, you can uncomment the test case in the script and run the script in a Python environment. 

```python
# Here's an example test case:
test_string = '(()()) ((())) () ((())()())'
expected_result = [2, 3, 1, 3]

result = parse_nested_parens(test_string)
print(result == expected_result)  # Output: True
``` 
The output should be `True` since the parsed result is equivalent to the expected result.  This indicates that the function is producing the correct output for the given input.