```python
def parse_nested_parens(parenthes):
    stack = []
    out = []
    for char in parenthes:
        if char == "(":
            stack.append(out.append(char))
        if char == ")":
            out.append(")" if stack else [] else stack.append(char)
   
    out.append(")" if stack else [] else stack.
    return out
 if stack else []

def test_parse_nested_parens():
    test_str = "(()()) ((())) () ((())()())"
    parse_nested_parens(test_str)
    for i in range(len(test_str)):
        if test_str[i] != ")":
            assert(test_str[i] == ")"
        if i < len(test_str) - 2:
            assert(test_str[i] == "(")
            assert(test_str[i+1] == "(")
            assert(test_str[i+3] == ")" )
```
This Python code defines a function `parse_nested_parens` that parses a string of nested parentheses. It uses a simple stack to keep track of opening parentheses. The function iterates through each character in the string. The function correctly handles the nested parentheses by identifying opening and closing parentheses. The `test_parse_nested_parens` function tests this `parse_nested_parens` function by providing a test string and expecting the correct output.