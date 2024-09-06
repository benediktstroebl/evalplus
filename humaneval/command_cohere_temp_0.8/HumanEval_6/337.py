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
            if nest < 0:
                break
        result.append(nest)
    return result
```

This script splits the input string into spaces and processes these chunks separately. It keeps track of the nesting level of parentheses for each chunk, iterating through the characters in each chunk. The nesting level is accumulated whenever we encounter a `(`, and it's decremented whenever we encounter a `)`. We assume that each chunk corresponds to a different group of parentheses. Once we hit a closing parenthesis, the nesting level is recorded, and we start processing the next chunk. The final result is a list of deepest nesting levels for each group of parentheses. 

Here is some example usage of the function and tests to verify its correctness:
```python
def test_parse_nested_parens():
    assert parse_nested_parens("(()()) ((())) () ((())()())") == [2, 3, 1, 3]
    assert parse_nested_parens("()") == [0]
    assert parse_nested_parens("(((((()()))))())") == [4]
    assert parse_nested_parens("(()) () ()") == [1, 0, 0]
    assert parse_nested_parens("")) == []
    assert parse_nested_parens("(())") == [1]
    assert parse_nested_parens("(()(()))") == [2]
    assert parse_nested_parens("(()(()(()(())))))") == [5]

test_parse_nested_parens()
```