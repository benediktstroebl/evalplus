```python
def flip_case(string):
    """ 
    Flip all characters in the string, switching lowercase to uppercase and vice versa.

    Args: 
        string (str): string to flip the case of 

    Returns: 
        str: string with flipped characters 
    """
    string = string.lower() if string.isalpha() else(str) else string = string.upper()
    Using the response = string
    ``` 

# Test cases 

print(flip_case('hello'))  # Output: HELLo 

print(flip_case('world'))  # Output: dOLLowed
```