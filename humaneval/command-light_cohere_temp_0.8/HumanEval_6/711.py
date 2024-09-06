```python
def parse_nested_parens(s: str) -> List[int]:
    def stack_parentheses(parentheses_string: str) -> List[int]:
        stack = []
        opening_brackets = {')': 0, '(': 1}
        
        for char in parentheses_string:
            if char in opening_brackets:
                stack.append(opening_brackets[char])
            continue
            if char == '(':
                stack.append(1)
            elif char == ')':
                stack.append(len)
                stack.append(opening_brackets[char])
        
        return stack
        
    return stack_parentheses(s)

def test_parse_nested_parens(input_str: str) -> None:
    stack = parse_nested_parens(input_str)
    expected_output = [2, 3, 1, 3]
    if stack == expected_output:
        print("Test passed.")
    else:
        print("Test failed.
```
This code defines a function `parse_nested_parens` that takes a string `s` as input and returns a list of integers representing the deepest level of nesting of parentheses in the string. The function uses a stack to track the opening and closing parentheses as it parses the string. It also defines a test_parse_nested_parens function, which takes an input string `input_str` and passes it to the `parse_nested_parens` function. This function is the test the input string to check if the output of `parse_nested_parens` matches the expected output.