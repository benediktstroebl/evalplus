```python
def separate_paren_groups(input_string):  # Define function to separate nested parentheses into individual strings
    return [p for p in input_string.split('([') for i, p in enumerate(input_string) if p == '(')])  # Use list comprehension to split the string into individual parentheses and their grouping

# Test cases
input_string = "( ) (( )) (( )( )) )"
assert separate_paren_groups(input_string) == ['()', '(())', '(()())']
input_string = ' ( )'
assert separate_paren_groups(input_string) == ['(']
input_string = "  (123'
assert separate_paren_groups(input_string) == ['123']
input_string = '{[(])}'
assert separate_paren_groups(input_string) == ['{[']}]']
```  This code demonstrates a function that takes a string of nested parentheses as input and splits it into individual parentheses. The function uses list comprehension to iterate over each parenthesis in the string, and if a parenthesis is '(', it is added to a new string in the list of results.