```python
def match_parens(lst):
    # Initialize the parentheses count for each type of parens
    open_count = close_count = 0
    
    # Iterate through each string in the list
    for s in lst:
        for c in s:
            if c == '(':
                open_count += 1
            else:
                close_count += 1
        
        # Check if the two strings can create a balanced string
        if open_count < close_count:
            return 'No'
        
        open_count = close_count = 0
    
    # If there are still open parentheses remaining, return 'No'
    if open_count > 0:
        return 'No'
    
    # If the loop completes without any issues, it's possible to create a balanced string
    return 'Yes'
```

This function takes a list of strings as input and returns a string indicating whether the two strings can create a balanced parentheses string when concatenated in some order. It correctly counts the number of open and closed parentheses and determines if any strings can create a valid concatenation.