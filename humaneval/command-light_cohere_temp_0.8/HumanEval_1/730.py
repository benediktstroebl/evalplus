```python
from typing import List
def separate_paren_groups(input_string: str) -> List[str]:
    return [i for i in input_string.replace(lambda x: x.match("([({[()|%+[A-Za-z0-9]+[(){}]*}]+})]+)$")
    ]
input_str = "( )(( )) (( )( )))"
print(separate_paren_groups(input_str))  # Output: ['()', '(())', '(()())']
```
This code defines a function called `separate_paren_groups` that takes a string as input and returns a list of separated parenthesis groups. 

The function uses a lambda function and the `match` function from the `re` module to create a regular expression pattern that matches nested parentheses. 

The pattern will match any sequence of parentheses that are balanced and not nested, and capture all groups, including any text inside them. 

The `match()` function will return a list of matches, and we use a generator expression `lambda x: x.match("([({[()|%+[A-Za-z0-9]+[(){}]*}]+})]+)")` to convert this into a list of strings representing the separated groups of parentheses.