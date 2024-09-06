```python
from typing import List

def parse_nested_parens(s: str) -> List[int]:
    result = []
    for bracket_level in reversed(list(map(len, s.split(' ') )))):
        result.append(bracket_level)
    return result
```

The reversed `map` function splits the input string into multiple strings using the space as a delimiter. Then, the length of each string is calculated, representing the bracket level, and stored in a list. The reversed function is used to return the list in the correct order. This way, you can easily retrieve the nesting level of each group of parentheses in the input string. 

To test this, run the following code:
```python
test_parse_nested_paren = {
    "'(()()) ((())) () ((())()())'": "[2, 3, 1, 3]",
    "'((()))': [2, 2]",
    "'()()': [1, 1]",
    "'(())': [1, 1]",
    "''": "[]",
}

for input_str, expected in test_parse_nested_paren.items():
    assert parse_nested_parens(input_str) == expected
```