```python
from typing import List
def parse_nested_parens(parenthes_str: str) -> List[int]:
    stack: List[int] = []
    curr_level = 0
    output: List[int] = []

    for char in parenthes_str:
        if char == " ":
            stack.append(curr_level)
            curr_level = 0
        elif char == "(":
            curr_level += 1
            stack.append(curr_level)
        elif char == ")":
            curr_level -= 1
            stack.pop()  #stack[-1] = curr_level
        else:
            stack.append(curr_level)
            curr_level = 0

    return output

# Test cases
def test_parse_nested_parens(test_str: str) -> None:
    assert parse_nested_parens("((()))") == [2, 3, 1, 3]
def test_parse_nested_parens_2(test_str: str) -> None:
    assert parse_nested_parens("(()())((()))") == [2, 3, 1, 3]
def test_parse_nested_parens_3(test_str: str) -> None:
    assert parse_nested_parens("(,())") == [1]")
def test_parse_nested_parens_4(test_str: str) -> None:
    assert parse_nested_parens("((()))") == []
def test_parse_nested_parens_5(test_str: str) -> None:
    assert parse_nested_parens("()()()())") == []
def test_parse_nested_parens_6(test_str: str) -> None:
    assert parse_nested_parens("((<>)")) == []")
```
The code defines a function called `parse_nested_parens` that takes a string as input and returns a list of integers representing the deepest level of nesting of parentheses in the string. The function uses a input string and stores parenthesis levels in a stack, then iterates through each character to determine the level of each parenthesis. Finally, the function returns the list of integers that represent the deepest level of nesting for each parenthesis encountered in the string.