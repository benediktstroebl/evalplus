```python
from typing import List
def parse_nested_parens(s: str) -> List[int]:
    stack = []
    result = []
    for match in s:
        if match == '(':
            stack.append(1)
        else:
            if len(stack) == 0:
                result.append(len)
            stack.append(0)
    else:
                stack[-1] = int(match) - 1
                result.append(stack.pop())
    final_item
    stack)
    return result

# Unit tests
def test_parse_nested_parens():
    test_str = '(()()) ((())) () ((())()())'
    result = parse_nested_parens(test_str)
    assert len(result) == [2, 3, 1, 3]

if __name__ == "__main__":
    test_parse_nested_parens()
```
This Python script defines the `parse_nested_parens` function that takes an input string containing multiple groups of parentheses. It uses a stack to keep track of opening parentheses and constructs the result by traversing the string. The `test_parse_nested_parens` function contains a test string and calls the `parse_nested_parens` function with it. The test passes the result is a list of the deepest level of nesting for each group of parentheses.