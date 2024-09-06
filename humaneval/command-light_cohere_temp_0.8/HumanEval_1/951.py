```python
from typing import List
def separate_paren_groups(s: str) -> List[str]:
    opening_braces = [')']
    closing_braces = [')']
    
    result = []
    stack = [s]
    
    while stack:
        if stack[-1].startswith('('):
            result.append(stack.pop(stack))
            closing_braces[0] = s[:-1]
            s = s[1:]
            stack.append(s)
        elif stack[-1].endswith(')'):
            result.append(stack.pop(stack))
            opening_braces.append(s)
            stack.append(s)
        else:
                next_brace = closing_braces.pop(stack)
                stack.append(next_brace) + s
        if len(stack) == 0:
                break
    
    return result

tests = [
    "Input: '() (( ) ) (( ) )'
        Output: ['()', '(())', '(()())']
    ",
    "Input: '( ) ( ) ) '()
    Output: ['()', '()', '()']
    ",
    "Input: '( )( ) )'
        Output: ['()', '((())')']
    ",
    "Input: '( ( ) ) )'
        Output: ['()', '()', '()']
    ",
    "Input: '()() ()'
        Output: ['()', '()', '()']
    ",
    "Input: '( ) ()'
        Output: ['()', '()']
    ",
    "Input: '( ( ) )'
        Output: ['(', '())', '()']
    ",
    "Input: '( ) ( ) ( )'
        Output) ['()', '()', '()', '()']
    "

def test_case(test_str):
    actual_result = separate_paren_groups(test_str)
    return str(actual_result) == ' '.join(map(lambda x: x.strip(), actual_result))
``` 
This code defines a function `separate_paren_groups` that takes a string of parentheses as input and returns a list of separated parenthesis groups. The function uses an opening and closing pair of parentheses to create a stack, and then iteratively pops elements from the stack and appends them to the result list. The test cases are a set of strings that the function is supposed to handle, and the function returns a boolean indicating whether it correctly handles each test case.