```python
def parse_nested_parens(s: str) -> List[int]:
    stack = []
    opening_level = 0
    closing_level = 0
    stack.append(opening_level)
    for match_str in s:
        if match_str == '(':
            closing_level += 1
        elif match_str == ')':
            closing_level -= 1
        else:
            opening_level += 1
    return stack.pop()
``` 
This Python function, parse_nested_parens, takes a string s as input and returns a list of integers. It performs a nested parentheses parsing by keeping track of opening and closing parentheses. It uses a nested stack data structure to store the deepest level of nesting. The stack is initially set to the opening level of the innermost most nested parentheses. 

Then, it iterates over the input string s. It increments the opening_level if it encounters '(' and decrements closing_level if it encounters ')'. It uses the stack.pop() function to get the most parenthesis group to return the deepest level of nesting of parentheses.