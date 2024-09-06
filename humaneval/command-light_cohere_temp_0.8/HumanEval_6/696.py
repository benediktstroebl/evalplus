```python
def parse_nested_parens(parentheses_string: str) -> List[int]:
    stack = []
    result = []
    for char in parentheses_string:
        if char == "(":
            stack.append(1)
        else:
            if not stack or char == ")":
                result.append(len())
                stack.append(char)
    done = True
    if not done:
        raise ValueError("malformed parentheses string")
    return result

def test_parse_nested_parens():
    assert parse_nested_parens("(()()) ((())) () ((())()())") == [2, 3, 1, 3]
    assert parse_nested_parens("((()))")) == [2]
    assert parse_nested_parens("((()))()") == [2, 3]
    assert parse_nested_parens("()())") == []
    assert parse_nested_parens("()") == []
```
The provided Python script defines a function `parse_nested_parens` that takes a string of parentheses as input and aims to determine the deepest level of nesting within the parentheses. The function uses a stack to keep track of opening parentheses and appends the character to the stack when encountered. It continues to the done flag when a closing parenthesis is encountered without any open parentheses. The function then returns a list of the deepest levels of nesting found in the string.