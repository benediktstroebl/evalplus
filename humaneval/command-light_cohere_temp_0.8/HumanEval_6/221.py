Here is a Python script that defines a function parse_nested_parens, which takes a string of nested parentheses as input and returns the deepest level of nesting for each group of parentheses:
```python
def parse_nested_parens(s: str) -> List[int]:
    def helper(match: str, index: int) -> int:
        if index == len(match):
            return 0
        opening, closing = match[index], match[index + 1]
        if opening == '(' and closing == ')':
            return helper(match, index + 2) + 1
        elif opening == ')' and closing == '(':
            return helper(match, index + 2) + 1
        else:
            return helper(match, index + 1) + 1

    match = []
    stack = []
    level = 0
    for char in s:
        match.append(char)
        if char == '(':
            stack.append('(')
        else:
            stack.append(')')
       
        match.append(char)

        if len(stack) == 0:
            return level
        stack.pop()
        max_level = helper(match, 0)
        for group in stack:
            level = max_level + (group == '(')
        return level

# Test cases
test_cases = [
    "(()()) ((())) () ((())()())",
    "((())()())",
    "((((()))))",
    "(()()()) ((()) ())",
    "()() ()() () ()",
    "((())()())()",
]

for case in test_cases:
    print(parse_nested_parens(case))
```
This script defines a function parse_nested_parens that takes a string of nested parentheses as input and returns the deepest level of nesting for each group of parentheses. The helper function is used to determine the depth of the nesting, and the main function uses a stack to keep track of opening and closing parentheses.