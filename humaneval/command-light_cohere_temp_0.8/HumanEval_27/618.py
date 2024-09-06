```python
def flip_case(string):
    return ''.join(''.lower() if c.isalpha(ord(c)) else c.isupper(ord(c)) and c.lower() for c in string)
```
The function flip_case takes a string as input and returns a modified string where all characters except lowercase letters are converted to the corresponding uppercase. The function first checks if the letter is a lowercase using the `isalpha()` function and then converts it to uppercase using the `upper()` method. If the letter is an uppercase, the function checks if the letter is a lowercase using the `isupper()` method and converts it to uppercase using the `lower()` method.