```python
from typing import List
def parse_nested_parens(s: str) -> List[int]:
    stack: List[int] = []
    result: List[int] = []
    for t in s:
        if t == '(':
            stack.append(1)
        else:
            stack.append(stack.pop()
            value, stack. 1995/10 a special to close. nested and a right group of parentheses can be accepted. Once the stack is empty, the function works its way backward and adds the value of the last element in the stack to the result list. 

# Test cases
test_cases = [
    "(()()) ((())) () ((()))()",
    "((((((()))))))))",
    "(((((((((()))))))))))))",
    "((()))() ((()))() ((()))()())",
    "((()())) ((())())",
    "(((((()))))))())",
    "(()()) ((())())",
    "(()())",
    "() () ((())())",
    "() ((())())",
]

for case in test_cases:
    result = parse_nested_parens(case)
    print(result)
    print(" ->", end="")
``` 

The script defines a function **`parse_nested_parens`** that takes a string of nested parentheses as input. It uses a simple stack-based technique to match each group of parentheses. It then returns a recursive list of deepest nesting parentheses found in the string. The test cases are printed to the console to ensure that the function is working as expected.