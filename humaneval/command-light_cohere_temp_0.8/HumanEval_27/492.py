```python
def flip_case(string):
    """For a given string, flip lowercase characters to uppercase and uppercase to lowercase."""
    # flip all characters in the string
    new_str = ''.join(c if c.isupper() else c.islower() else c else c.islower() else c else c
       
    return new_str

# Test the function
print(flip_case('hello'))  # Output: HELLo 

print(flip_case('HOelder'))  # Output: august 

print(flip_case('HeLLo'))  # Output: hello 

```