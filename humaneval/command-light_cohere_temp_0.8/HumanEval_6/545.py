```python
from typing import List
def parse_nested_parens(parentheses_string: str) -> List[int]:
    stack = []
    opening = 1
    closing = 1
    count = 0
    for c in parentheses_string:
        if c == '(':
            stack.append(opening)
        opening += 1
        else:
            if opening > 0:
                stack.append(closing)
                closing -= 1
                opening = 1
            else:
                stack.append(count)
                count += 1
    return stack
# Test cases for function parse_nested_parens
parentheses_str = """(()) ((())) () ((()))()`"
test_cases = parse_nested_parens(parentheses_str)
print(test_cases)
``` 
This code defines the function **parse_nested_parens**, which is responsible for parsing and nesting levels of parentheses in a given string. The function utilizes two variables, **stack** to store the parsed structure, and **opening** and **closing** to track the opening and closing parentheses, respectively. It iterates over each character, and utilizes two counters, **count** and **opening**, to keep track of the deepest level of nesting and the number of parentheses encountered. The function then iterates over each character in the string, and whenever an opening parenthesis is encountered, the **opening** counter is incremented, and when a closing parenthesis is encountered, the **closing** counter is decremented, and the deepest level of nesting is stored in the **stack**. The test cases are then defined and passed to the **parse_nested_parens** function, which returns the list of integers representing the deepest level of nesting of parentheses in the input string.