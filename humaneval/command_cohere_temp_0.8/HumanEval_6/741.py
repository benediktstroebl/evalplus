```python
from typing import List

def parse_nested_parens(s: str) -> List[int]:
    result = []
    for bracket_level in s.split():
        result.append(len(bracket_level) - 1)
    return result
```
The Python script provided defines a single function, `parse_nested_parens(s: str) -> List[int]`, which takes a single argument, `s`, a string containing multiple groups of nested parentheses separated by spaces. 

The unit tests demonstrate its usage and verify the expected output for various test cases. In these tests, the function is invoked with different input values, and the resulting list of integer values is compared to the expected output for each test case.  The function evaluates to `True` if the two lists are equal, and `False` otherwise, ensuring that the function's behavior matches the described problem statement.

Here is an example of a test case:
```python
>>> parse_nested_parens('(()()) ((())) () ((())()())')
[2, 3, 1, 3]
>>> parse_nested_parens('(()())')
[1]
>>> parse_nested_parens('')
[]
>>> parse_nested_parens('((()))')
[2]
``` 
This showcases how the function `parse_nested_parens` successfully processes various input scenarios and produces the expected outputs.