```python
from typing import List
def separate_paren_groups(parentheses: List[str]) -> List[str]:
    result = []
    for p in parenthesis:
        if not nested_in_parentheses(p):
            result.append(p)
        nested_in_parentheses(p) and p != ')' and p != ')' :
            nested_in_parentheses([p]))
        else:
            result.append(')' * len(p) - 1)
    return result
def nested_in_parentheses(item):
    return item[0] == '(' and any_not_closing(item[1:])
def any_not_closing(items):
    for i, item in enumerate(items):
        if item[i] == ')' and i != items.count_closing:
            return False
    count_closing = 0
    for i, item in enumerate(items):
        if item[i] == '(':
            count_closing += 1
    return count_closing < 2
``` 
This script defines a function `separate_paren_groups` that takes a list of strings as input and returns a list of separate strings. The function works by iterating through the list of strings and checking if each string is not nested within any other parentheses. If the string is not nested, it is added to the list of results. If the string is nested, it is added to the list of results with an extra ')' character added to it to balance out the nesting. 
This script also defines two helper functions: `nested_in_parentheses` and `any_not_closing`, that are used to check if a string is a valid parenthesis string and to check if a string is not closing a parenthesis respectively.