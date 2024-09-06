```python
from typing import List
def separate_paren_groups(parenthesis: str) -> List[str]:
    return [p.split('() for p in parenthesis.split(' ')[0] if p else '()]' and p.split('() in') else p for p in parenthesis]

# Test cases
parentheses_test = '''
( ) (( )) (( )( ))'
()()()()()
( ) ) ( () ) 
(((())))'''

print(separate_paren_groups(parentheses_test))
``` 
This Python code defines a function `separate_paren_groups` that splits a given string into a list of parentheses. The function utilizes the string slicing and list comprehension to achieve this. The function is then tested with a test string containing various scenarios, and the output is printed.