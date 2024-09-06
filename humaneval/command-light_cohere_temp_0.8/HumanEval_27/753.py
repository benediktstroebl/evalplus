```python
def flip_case(string):
    return ''.join(''.lower() if c.isalpha(ord(c)) else c.isupper(ord(c)) else c) for c in string)
``` 
This function takes a string `string` as input and returns a new string where the characters are flipped from lowercase to uppercase and vice versa. The function uses the own iteration to go through each character in the string, and uses the `ord()` function to check if the character is a lowercase letter, and returns the character in uppercase if it is. This ensures that the characters that are not letters will remain unchanged.