```python
def separate_paren_groups(parentheses: str) -> List[str]:
    return [p.join() for p in parentheses.
    where parentheses = '()' + '([') + '((' + ')(' + ')') + ')'. 

def test_separate_paren():
    assert separate_paren_groups('( ) (( )) (( )( ))') == ['()', '(())', '(()())']
```
This script defines a function `separate_paren_groups` that splits a string of parentheses into individual groups. The test_separate_paren function asserts that the output of the `separate_paren_groups` function is correct, i. each. You can add this have test way for this code's functionality.