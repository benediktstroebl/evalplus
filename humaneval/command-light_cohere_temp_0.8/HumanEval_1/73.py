```python
from typing import List
def separate_paren_groups(s: str) -> List[str]:
    result = []
    stack = []

    for char in s:
        if char == '(': stack.push('')
        if char == ')': stack.pop()
       group() = [char]
        result.append(char)

    return result
    ``` 
This function, separate_paren_groups, takes a string s as input and returns a list of separated parenthesis groups. The function uses a nested while loop to iterate through each character in the input string. The goal is to separate each group of parentheses into separate strings and return the list of those strings.