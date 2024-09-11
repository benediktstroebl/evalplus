```python
def flip_case(string: str) -> str:
    """ For a given string, flip lowercase characters to uppercase and uppercase to lowercase.
    >>> flip_case('Hello')
    'hELLO'
    """
    result = ""
    for char in string:
        if char.islower():
            result += char.upper()
        elif char.isupper():
            result += char.lower()
    return result

# Test the function
print(flip_case('Hello'))
```

This script defines a function `flip_case` that iterates over each character in the input string. If the character is lowercase, it converts it to uppercase and adds it to the result. If the character is uppercase, it converts it to lowercase and adds it to the result. The final result is then returned and printed to the console.