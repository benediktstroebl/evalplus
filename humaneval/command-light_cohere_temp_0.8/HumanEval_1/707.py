Here's a self-contained Python function that solves the problem you described: 

```python
def separate_paren_groups(s): 
    """ 
    Input to this function is a string containing multiple groups of nested parentheses. 
    Separate groups and balanced (each open brace is properly closed) and not nested within each other. 
    Return the  a list of those separated strings. 
    """ 
    balance = False 
    new_group = ''
    result = []
    
    for char in s:
        if char == '(': 
            balance = True
        elif char == ')':
            balance = False
        
        if balance: 
            new_group += char
            if not balance: 
                result.append(new_group)
                new_group = ''
            
        else: 
            new_group += char
    
    return result
```

This function takes a string `s` as input and iterates through each character in the string. When an open parenthesis `( )` is encountered, the function marks it as the start of a new group and adds it to the `new_group`. It then checks if the current character is the right parenthesis `)`. If it's not, the function adds the current character to the `new_group` string and marks the balance as False. If it's adds a character that is not a parenthesis, it adds the character to the `new_group` string. The `balance` variable is set to True after the current character is processed. This will continue until all character is a parenthesis.