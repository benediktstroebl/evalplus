Here is a self-contained Python script that solves the problem of recognizing the deepest level of nesting of parentheses in a given string:
```python
def parse_nested_parens(s):
    stack = []
    temp = ""
    for char in s:
        if char == "(":
            stack.append(")" if temp != "" else temp + "("
            temp = ""
        elif char == ")":
            if temp == "" :
                stack.append(")"
                else
                temp += ")"
        else:
            temp += char
    return stack

def test_parse_nested_parens(test_str):
    assert parse_nested_parens(test_str) == [3, 1, 3] # Test with valid string

# Test with invalid string
test_str = "(()()) ((())) () ((()))()"
assert parse_nested_parens(test_str) == [2, 3, 1, 3]
```
This script defines a function parse_nested_parens that takes a string as input and returns a list of depths of nesting of parentheses. It uses a nested "()" and ")" characters to represent the structure of the string. The function uses a stack data structure to keep track of the open parentheses, and a counter variable to track the closing parentheses. It starts by iterating over the characters in the string, and if a "(" character is encountered, it appends the corresponding ")" to the stack if the counter variable is not empty. If a counter is empty, the function appends the ")" to the stack. Finally, if a closing ")" character is encountered, the function appends the ")" to the stack. The function returns the stack data structure.