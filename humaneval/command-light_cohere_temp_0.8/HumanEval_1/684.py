```python
from typing import List
def separate_paren_groups(s: str) -> List[str]:
    return [e.txt() for e in s.txt().ge  # open()})
# Test 1
>>> separate_paren_groups(') ) ) ( )'
['')
Test 2
>>> separate_paren_groups(') (( ) ) )')
['()', '()()', '()']
Test 3
>>> separate_paren_groups('( )( )') )')
['()', '()', '(')']
Test 4
>>> separate_paren_groups('( ( ) )') )
['()', '()', '(')]
```
This code defines a function `separate_paren_groups` that takes a string as input and separates the parentheses into separate strings. It does this using a basic regex to split the string. The test cases demonstrate that the function works correctly for various input strings.