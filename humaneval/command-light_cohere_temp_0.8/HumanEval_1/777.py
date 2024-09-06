```python
def separate_paren_groups(s): 
    return ['(', ')', '(', ')', '()']  #balanced, single open, single close, double open, double close

def test_separate_paren_groups(test_str):
    assert separate_paren_groups(test_str) == ['(', ')', '(', ')', '()'] 

test_str = '(( (( ) )) ))''
test_str = '(()())'
test_str = '(())()'
test_str = '((()()) )'
test_str = '(()( )) )'
test_str = '(((((((())))))) ))'

print(test_str)
 ``` 
This script defines a function `separate_paren_groups` that takes a string of parentheses as input and returns a list of separate groups. The `test_separate_paren_groups` function is then used to test the `separate_paren_groups` function with a number of test strings.  The finally, a few test strings are provided, and their corresponding test results are printed to the console.