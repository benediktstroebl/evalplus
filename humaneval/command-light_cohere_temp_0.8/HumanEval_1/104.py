```python
from typing import List
def separate_paren_groups(s: str) -> List[str]:
    return [i for i in s.open() if i != ')' and i != '(']

# tests
tests = [
    'Input: (() ) (( )) (( )( ))'
    'Expected Output: ([(),())', '()())', '(()())']
    '
 
    'Input: ( )()  ()()'
    'Expected Output: ([(),())']
    '
 
    'Input: ( () ) ()'
    'Expected Output: ([(),())']
    '
 
    'Input: (( ) ) ())'
    'Expected Output: ([()), ('())')
    '
 
    'Input: ( ( ) ) )'
    'Expected Output: ([(),())'
    '
 
    'Input: ( ( )) ) )'
    'Expected Output: ([(),())'
    '
 
    'Input: (( )) ) )'
    'Expected Output: ([()), ('())')
    '
 
    'Input: (( () ) ) )'
    'Expected Output: ([(),())'
    '
  ]
```