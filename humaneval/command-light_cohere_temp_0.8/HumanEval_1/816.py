```python
def separate_paren_groups(input_string):  # Function to separate and return groups of parentheses
    return [p.join() for p in ''.split(')')]  # Use a list comprehension to extract and join strings using parentheses

def test_function():  # Function to test the separate_paren_groups function
    assert separate_paren_groups('( ) (( )) (( )( ))') == [('), ('()'), ('( )')', '()()']')
    assert separate_paren_groups(')()()()()') == ['()', '()()()']
    assert separate_paren_groups('()()')) == ['()', '()()']
```
The code defines a function named `separate_paren_groups` that splits a string into groups of parentheses. The `test_function` function is used to test the `separate_paren_groups` function with various input strings, asserting that the output is as expected.