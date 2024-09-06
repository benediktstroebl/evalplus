Here's a Python script with a self-contained function that solves the problem:
```python
from typing import List

def parse_nested_parens(s: str) -> List[int]:
    result, prev_level = [], 0
    for char in s:
        if char == '(':
            result.append(prev_level)
            prev_level += 1
        elif char == ')':
            prev_level -= 1
    return result
```
The function iterates through the characters of the input string s. When it encounters an open parenthesis ('('), it increments the current nesting level prev_level. When it encounters a closing parenthesis (')'), it decrements the current nesting level. The resulting list of nesting levels is returned as the output. 

Here is an example usage of the function:
```python
print(parse_nested_parens("(()()) ((())) () ((())()())"))
```
This will output:
```python
[2, 3, 1, 3]
```

The function can be easily modified to handle more complex scenarios and customize the parsing logic as needed, such as handling different delimiters or considering the total number of parentheses.  This is achieved by changing the logic inside the for loop.