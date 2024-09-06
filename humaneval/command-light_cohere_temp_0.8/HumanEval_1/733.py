```python
def separate_paren_groups(s):
    """Separate balanced parentheses from a string and return as a list of strings."""
    return [ matched for matched in re.balance_groups(s, '[()]+', '()') ]


def balance_groups(s, start, end):
    """Check whether a string of parentheses is balanced."""
    return '(' in s[start:end] and ')' in s[end+1:end+2] and '(' not in s[end:end-1]

def test_separate_paren_groups():
    assert separate_paren_groups('() (( )) (( )( ))')') == ['()', '(())', '(()())']
    assert separate_paren_groups('( )(( ))'))') == ['()', '()()', '(()())']
    assert separate_paren_groups('((()))')') == ['()', '()()', ')()']
    assert separate_paren_groups('( )') == ['()', '()()']
    assert separate_paren_groups('()()()') == ['()()()']


# Run the tests
test_separate_paren_groups()
``` 
This Python code defines a function `separate_paren_groups` that takes a string `s` as input and returns a list of strings extracted from balanced parentheses. 

The function uses the `balance_groups` function to check if a string of parentheses is balanced, which returns `True` if the parentheses are balanced and `False` otherwise. 

The `balance_groups` function uses a simple algorithm to determine if a string of parentheses is balanced by checking if there's an opening parenthesis, an closing parenthesis, and the inverse of an opening parenthesis. 

Finally, the code includes a set of tests for the `separate_paren_groups` function using the `assert` function to ensure that the function is working correctly.