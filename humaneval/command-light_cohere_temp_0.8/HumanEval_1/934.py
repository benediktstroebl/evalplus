```python
from typing import List
def separate_paren_groups(input_str): 
    brackets = [p for p in input_str if p == '(']
    brackets.extend(brackets) = []
    for bracket in brackets:
        nested = [p for p in input_str if p == '(']
        brackets.extend(nested)
    result = [''.join(bracket) if bracket else ']
    return result
input_str = '( )(( )) (( )( ))'
print(separate_paren_groups(input_str))
``` 
The code defines a function `separate_paren_groups`, which takes a string as input and aims to separate out nested parentheses. It uses a specific characters to identify parentheses and creates a list of these groups. The nested list is then expanded to include any inner parentheses, creating a new list of strings. The final result is a list of strings with balanced parentheses, which are then returned by the function.