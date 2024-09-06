```python
def flip_case(string: str) -> str:
    """ 
    Convert a given string to have all characters flipped between lowercase and uppercase 
    """ 
    return string.upcase(string.lower()) if string.isalpha(string) 
    if not (isalpha(string)) : 
        raise ValueError("Input string is not valid, it must contain only alphabetic characters")
    else: 
        return string.upcase(string.isupper(string))
```

This script defines a `flip_case` function that takes a string as input and returns a new string with all characters flipped between lowercase and uppercase. It uses the string. If the input string is not a valid alphabet, it raises a ValueError.