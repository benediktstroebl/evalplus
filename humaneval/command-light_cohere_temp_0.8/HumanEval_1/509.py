```python
from typing import List

def separate_paren_groups(parenthes: str) -> List[str]:
    return [c for c in parents if c == ')' or ')']

parent_string = '((()))'
result = separate_paren_groups(parent_string)
print(result)
```
This script defines a function **separate_paren_groups** that takes a string of parenthesis-containing text as input and returns a list of separated parentheses.  The function uses a list comprehension to iterate over each character in the input string, and if the character is either a ')' or ')' character, it is added to the result list. 

In this improved solution, we use the built-in function **str.join** to convert the string to a list of characters.