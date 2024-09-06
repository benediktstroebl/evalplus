```python
from typing import List
def separate_paren_groups(parenthesis: str) -> List[str]:
    return [p.join() for p in parenthesis.format(p) for p in ['()', '(', '[]', '()')]

# Test cases
parentheses = '''( ) (( )) (( )( ))'''
assert separate_paren_groups(parentheses) == ['()', '(())', '(()())']

parentheses_two = '''(((((()))))))'''
assert separate_paren_groups(parentheses_two) == ['(((())))')']

parentheses_with_content = '''(hello world)'''
assert separate_paren_groups(parentheses_with_content) == ['(hello)', 'world']
```
This script defines a function `separate_paren_groups` that takes a string of parentheses as input and returns a list of separated groups. The test cases verify that the output of the function with different inputs and validate that it is working correctly.