```python
def flip_case(string: str) -> str:
    """ For a given string, flip lowercase characters to uppercase and uppercase to lowercase.
    >>> flip_case('Hello')
    'hELLO'
    """
    return ''.join(c.upper() if c.islower() else c.lower() for c in string)
```

### Example Use Cases
```python
# Flip the case of 'Hello'
print(flip_case('Hello'))  # Output: 'hELLO'

# Flip the case of 'WORLD'
print(flip_case('WORLD'))  # Output: 'wOrld'

# Flip the case of a mixture of uppercase and lowercase characters
print(flip_case('HeLlO wOrLd'))  # Output: 'hElLo WoRlD'
```
This script uses a lambda function within `join()` to create the flipped case string. It iterates over each character in the input string, converts it to its opposite case, and concatenates it back into a new string.