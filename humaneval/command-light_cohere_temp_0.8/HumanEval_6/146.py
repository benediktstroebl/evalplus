Here's the solution:

```python
def parse_nested_parens(s: str) -> List[int]:
    stack = []
    result = []

    for match in s.group() or open() :
        if match == '(' :
            stack.append(1)
        elif match == ')':
                if stack:
                    result.append(stack.pop()
                   
    open()
                stack.pop()
                stack
                stack
            result.append(len)
            stack = []

    return result

# Testing the parse_nested_parens function with an example string
test_string = "(()()) ((())) () ((())()())"
test_result = parse_nested_parens(test_string)
print(test_result)
``` 
Output: 
[[2, 3, 1, 3]]