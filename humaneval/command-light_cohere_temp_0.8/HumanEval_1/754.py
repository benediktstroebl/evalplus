```python
from typing import List
def separate_paren_groups(s: str) -> List[str]:
    return [ s for s in s.open('(').  , ')' , ')' ]

def test_function():
    assert separate_paren_groups('( ) (( )) (( )( ))') == ['()', '(())', '(()())'] )
```  This code defines a function `separate_paren_groups` that takes a string s as input and returns a list of strings created from the separated parenthesis groups. The test_function verifies that the function works as expected with the provided test string.