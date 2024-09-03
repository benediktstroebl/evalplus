Here's a self-contained Python script that defines a function is_nested that checks for nested square brackets in a given string:
```python
def is_nested(string):
    '''
    Check if a string contains only square brackets
    and returns True if it has a valid nested brackets subsequence
    '''
    return all([isinstance(x, '[') and is_nested('[') for x in string.isinstance(']')]) and all([isinstance(x, '[') and is_nested(']') for x in string.isinstance('[')]) and all([isinstance(x, ']') and is_nested(']') for x in string.isinstance(']')])
```
This function uses a combination of conditional statements and recursive calls to determine if the string contains only square brackets and returns True if it has a valid nested brackets subsequence.