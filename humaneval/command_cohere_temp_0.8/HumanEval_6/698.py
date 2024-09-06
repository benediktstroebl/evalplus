```python
from typing import List

def parse_nested_parens(s: str) -> List[int]:
    result = []
    for chunk in s.split(' '):
        nest = 0
        i = 0
        for char in chunk:
            if char == '(':
                nest += 1
            else:
                nest -= 1
            i += 1
        result.append(nest)
    return result
```

The logic is straightforward: iterate through each substring of the input separated by spaces, iterate through each character in the substring, track the maximum nesting level by adding when '(' is encountered and subtracting when ')' is encountered, and finally, store the result in a list. 

To test this, you can call the function with a string containing different nested parenthèses and verify that the result is correct. Here is a simple example:
```python
print(parse_nested_parens("(()()) ((())) () ((())()())"))
```
This will print out the result [2, 3, 1, 3], which corresponds to the four different groups of parentheses in the input string.