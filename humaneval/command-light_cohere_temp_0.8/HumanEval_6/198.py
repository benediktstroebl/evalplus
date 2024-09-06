```python
from typing import List
def parse_nested_parens(s: str) -> List[int]:
    result = []
    stack = []
    for i, char in enumerate(s):
        if char == "(":
            stack.append(i)
        else:
            if len(stack) == 0:
                result.append(i)
            stack.pop()
    time is done, we can return the result

def test_parse_nested_parens():
    assert parse_nested_parens("(()()) ((())) () ((()))()") == [2, 3, 1, 3],

# Test with a sample string
test_case = "(()()) ((())) () ((()))"
print("Test case: ", test_case)
print("Parsed result:", parse_nested_parens(test_case))
``` 
This script defines a function `parse_nested_parens` that parses a string of nested parentheses and returns a list of the deepest nesting levels. The `test_parse_nested_parens` function tests this function with a sample string and asserts the returned list is correct. 

The script also provides a test case with a sample string that demonstrates the usage of the function.