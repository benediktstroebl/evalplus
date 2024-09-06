```python
def separate_paren_groups(parenthesis_string):  # Updated docstring to reflect the change from List to str
    return [p.format('(' + s + ')', end='') for s in parenthesis_string.format(')', end='')
```
This code defines a function named `separate_paren_groups` that takes a string containing multiple groups of parentheses as input and returns a list of strings where each group of parentheses is separated. The function uses the `str` to build a new string by adding the open parentheses to the string `s` (which may contain other strings with parentheses) and then concatenates the result with the closing parenthesis.