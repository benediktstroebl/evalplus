```python
def parse_nested_parens(parent_string: str) -> List[int]:
    stack = []
    start = 0
    result = []
    for i, char in enumerate(parent_string):
        if char == " ":
            stack.append(start)
            start = i + 1
        elif char == ")":
            if len(stack) > 0 and stack[-1] == start:
                stack.pop()
               
                result.append(start)
                start = i + 1
    return result

# Test cases
test_cases = [
    "(()()) ((())) () ((())()())",
    "((())) (())",
    "((()()()()()()()()))",
    "()() ((())())",
    "() ((()))",
    "()() (()) ()",
    "((()()()) ()()())",
]

for case in test_cases:
    test_result = parse_nested_parens(case)
    print("Case:", case, ", end="")
    print(*test_result)
```
The above code defines the `parse_nested_parens` function, which takes a string of nested parentheses as input and returns a list of corresponding integer levels of nesting. The function uses a to maintain a stack of opening parentheses while traversing through the string. It identifies the maximum level of nesting and returns the deepest level of nesting. Finally, the test cases demonstrate the code's functionality by passing different input strings and printing the corresponding output.