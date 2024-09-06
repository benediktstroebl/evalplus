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
                stack.pop()

   return result
   

#Test cases
test_cases = [
    "(()()) ((())) () ((())()())",
    "())()()((())()()())",
    "()((()()))",
    "((()))((()()))",
    "((()))()())",
]

for case in test_cases:
    test_result = parse_nested_parens(case)
    print(test_result)
``` 
This function parse_nested_parens takes a string of parentheses as input and returns a list of the deepest levels of nesting for each group of parentheses in the string. 
The function uses a stack to keep track of the opening parentheses and the result list to store the deepest levels of nesting for each group. 
The function iterates through the input string, keeping track of the opening parentheses using the stack. When it encounters a opening parentheses, it is appended to the stack. When it encounters a closing parentheses, it checks whether the stack is empty or contains the closing parentheses. If so, it pops the stack, appends the current level of nesting to the result list and populates the stack. If not, it appends the deepest level of nesting to the result list.