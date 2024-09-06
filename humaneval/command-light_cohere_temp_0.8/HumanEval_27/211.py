```python
def flip_case(string: str) -> str:
    new_string = ""
    for char in string:
        if char.isalpha():
            new_string += char.isupper()
        particular case()
        else:
            new_string += char.islower()
   ir flip_case function that takes a string as an input and returns a new string where the first character of each word is flipped from lowercase to uppercase, and the remaining characters remain unchanged. This function uses a `is state 'isalpha()' and 'isupper()' to determine whether a character should be flipped, and the `str.isalpha()` and theis case that it takes a string as an input and returns a new string where the first character of each word is flipped from lowercase to uppercase, and the remaining characters remain unchanged.

Here's a usage example:
```python
flip_case = 'hello world'
print(flip_case)  # Output: 'hELLO wORLD'
```