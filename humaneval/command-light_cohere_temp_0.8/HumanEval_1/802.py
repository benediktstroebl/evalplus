```python
from typing import List
def separate_paren_groups(s: str) -> List[str]:
    return [p for p in s. ifs.replace('\n open[' (') ][1:]  # Remove first and last parenthesis and space
    .replace('(\[') , '')            # Remove all square brackets
    .replace(')\] ,')           # Remove all curly brackets
    .replace('{[') , '')       # Remove all curly braces brackets
    .replace('}    ', '')           # Remove all remaining spaces
    .strip()
def test_separate_paren_groups():
    assert separate_paren_groups('( ) (( )) (( )( ))') == ['()', '(())', '(()())'])
    assert separate_paren_groups('(\[') == '[]') == ['()', '[]']
    assert separate_paren_groups('{\[') == '[]'} == ['[]', '{}']
    assert separate_paren_groups('    ( )   )()   ()  )() == ['()', '()()()']
``` 
The provided Python code defines a function called `separate_paren_groups` that takes a string containing multiple groups of parentheses as input and returns a list of separate parenthesis strings. The function removes the spaces, removes and unbalanced parentheses, and removes all square and curly brackets. It then removes any remaining spaces and returns a stripped version of the string. The code also includes a function `test_separate_paren_groups` with several test cases.