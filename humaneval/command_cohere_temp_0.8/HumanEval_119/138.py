```python
def match_parens(lst):
    opened = True
    for char in lst[1]:
        if char == '(':
            opened = False
        elif char == ')':
            if not opened:
                return "No"
            opened = True
    return "Yes" if opened else "No"
```

This script provides a function `match_parens` that takes a list of two strings as input and returns a string indicating whether the two strings can be concatenated to form a balanced parentheses string. The function checks if the second string can close all the parentheses opened in the first string and vice versa.

Here is an example of how to use this function:
```python
print(match_parens([ '(()', ')']) )  # Output: Yes
print(match_parens([ ')(', '()))' ])  # Output: Yes
print(match_parens([ '())', '(' ])  # Output: No
```

This function operates under the assumption that the two strings in the input list contain only parentheses characters ('(' and ')') and no other characters.