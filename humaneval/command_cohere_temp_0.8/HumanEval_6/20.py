```python
from typing import List

def parse_nested_parens(s: str) -> List[int]:
    result = []
    for segment in s.split():
        depth = 0
        nesting = 0
        i = 0
        for i, char in enumerate(segment):
            if char == '(':
                nesting += 1
            elif char == ')':
                nesting -= 1
            if nesting < 0:
                break
            depth = max(nesting, depth)
        result.append(depth)
    return result
```
The function iterates through each segment of the string, maintaining a 'depth' variable that keeps track of the maximum nesting level of parentheses encountered so far in that segment. It accumulates the result and returns it as a list of integer depths. 
The unit tests are correctly placed to ensure the function behaves as expected. It first tests the function with a simple input and then an input that includes multiple parentheses groups separated by spaces. 
The expected output for the latter is a list of depths corresponding to each group. 
```python
test_parse_nested_parens = {
    "input": "(()()) ((()))",
    "output": [2, 3]
}

test_parse_nested_parens_2 = {
    "input": "(()()) ((())) () ((())()())",
    "output": [2, 3, 1, 3]
}
``` 
These test dictionaries are then used in the test suite using the `assert_equal_lists` function:
```python
def test_parse_nested_parens():
    assert_equal_lists(parse_nested_parens(test_parse_nested_parens["input"]), test_parse_nested_parens["output"])

def test_parse_nested_parens_2():
    assert_equal_lists(parse_nested_parens(test_parse_nested_parens_2["input"]), test_parse_nested_parens_2["output"])
``` 
This test suite will ensure that the function behaves as expected, accurately parsing the deepest level of nesting for each group of parentheses in the provided input.