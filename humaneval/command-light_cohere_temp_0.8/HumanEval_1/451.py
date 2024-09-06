```python
def separate_paren_groups(s): 
    return ['()' for i in s. p if ')' in i and '(' not in i] + ['('] * (len(')' - len('(')))]

# Driver code to test the function
test_string = '() (( )) (( )( ))'
print(separate_paren_groups(test_string)) 
```
Do you have a solution to the problem that you can use in your markdown code block?