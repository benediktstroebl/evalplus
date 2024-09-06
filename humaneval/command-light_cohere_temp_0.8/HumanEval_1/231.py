```python
def separate_paren_groups(input_string):
    """
    Separate groups of balanced parentheses.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    # Use nested loops to separate groups
    left, right = 0, 0
    result = []
    while left < len(input_string) or right < len(input_string):
        if input_string[left] == '(' and input_string[right] == ')' :
            result.append(input_string[left:right])
            left += 1
            right += 1
        elif input_string[left] == ')' and input_string[right] == '(' :
            right -= 1
        elif input_string[left] == ' ' :
            left += 1
        else:
            right -= 1
    return result
```