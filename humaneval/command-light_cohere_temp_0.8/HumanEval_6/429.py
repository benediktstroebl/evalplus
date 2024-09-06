```python
def parse_nested_parens(parenthes):
    stack = []
    output = []
    for char in parenthes:
        if char == "(": stack.append(char)
        elif char == ")":
            if stack:
                output.append(stack.pop()
            stack.else: [char]
    stack = []
    return output

#Test cases
assert parse_nested_parens('(()()) ((())) () ((())()())') == [2, 3, 1, 3])
assert parse_nested_parens(')()) () () ((())()())') == [2]
assert parse_nested_parens('(,()) () ((())()()))') == [1]
assert parse_nested_parens('()()) ()') == []
``` 
The provided Python script defines a function `parse_nested_parens` that takes a string of nested parentheses as input and returns a list of the deepest levels of nesting. It uses a stack to keep track of opening parentheses and iterates over the string, appending the current opening parenthesis to the stack and then popping it to the output list when a closing parenthesis is encountered. 

The test cases in the script verify the function's correctness by passing different input strings and checking if the returned output matches the expected result.