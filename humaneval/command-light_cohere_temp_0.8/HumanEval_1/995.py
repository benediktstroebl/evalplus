```python
def separate_paren_groups(s): 
    return [token for token in s.group if ')' in token and '(' not in token]

def test_function(): 
    pass_group = "( )"
    assert separate_paren_groups(pass_group) == ['()'] 
    text_group = "(( (( )) )))"
    assert separate_paren_groups(text_group) == ['()', '(())'] 
``` 
This code defines a function `separate_paren_groups` that takes a string `s` as input and returns a list of substrings tokenized from the string. The `test_function` function tests the validity of the `separate_paren_groups` function by passing test cases.