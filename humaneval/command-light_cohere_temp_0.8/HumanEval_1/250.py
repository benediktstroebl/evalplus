```python
def separate_paren_groups(s):
    return ['(' + c + ')' for c in s.
    if any:
        raise ValueError('Input string must contain groups of parentheses')

def test_function():
    assert separate_paren_groups('( ) (( )) (( )( ))') == ['()', '(())', '(()())'])
    assert separate_paren_groups('( ) (( ()) )') == ['()', '(', '()', '()'])
    assert separate_paren_groups('[())') == ['[', ']')
    assert separate_paren_groups('( [] ))') == ['()', '()()')
    assert separate_paren_groups('{[(]) }') == ['{', '}')
    assert separate_paren_groups('()()()') == ['()', '()()']
    assert separate_paren_groups('( )') == ['()']

if __name__ == "__main__":
    test_function()
```
This script defines a function `separate_paren_groups` that takes a string as input and returns a list of separated parentheses. 

The `test_function` function contains a number of test cases that validate the correctness of the `separate_paren_groups` function. 
In the `__name__` == “main” block, the code runs the `test_function` to ensure the function works correctly.