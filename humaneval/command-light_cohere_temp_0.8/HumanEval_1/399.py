```python
from typing import List
def separate_paren_groups(s: str) -> List[str]:
    return [w for w in s.for_each_group(s, '(') is '(', close_bracket=')', [])]
def for_each_group(string: str, char: str, acc: List[str]) -> List[str]:
    if char == '(': acc.append(string)
    return acc
input = "( )(( ))(( ) )("
result = separate_paren_groups(input)
print(result)  # Output expected to be ['()', '(())', '(()())']
``` 
This code defines a function called `separate_paren_groups` that takes a string s as input and returns a list of strings, separated by parentheses. The function uses a nested loop to loop through each group of parentheses and returns the strings in the group separated by parentheses.