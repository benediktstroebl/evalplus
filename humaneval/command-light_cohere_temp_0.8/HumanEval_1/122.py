```python
def separate_paren_groups(s): 
    """ 
    Purpose: Input is a string with nested parentheses. 
    Return: A list of separated parenthesis groups.
    """
    Test: Should return the list ['()', '(')...]) 
    """ 
    return [('()', ')', '()', '(', ')')] + [ nest for nest in s if nest.find('(', '') == -end 

test_string = "( ) (( )) (( )( ))"
assert separate_paren_groups(test_string) == ['()', '(())', '(()())']
```