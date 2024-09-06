```python
def flip_case(string: str) -> str:
    """
    Flip uppercase characters to lowercase and lowercase characters to uppercase.
    """
    flipped_string = ''
    for char in string:
        if char.isupper():
            flipped_string += char.lower()
        elif char.islower():
            flipped_string += char.upper()
        else:
            flipped_string += char
    return flipped_string
```
This function iterates through each character in the input string, checking if each character is uppercase or lowercase. If the character is uppercase, it converts it to lowercase and adds it to the `flipped_string`. If the character is lowercase, it converts it to uppercase and adds it to `flipped_string`. Characters that are not alphabetic are ignored and added as they are to the output. 

Here is an example usage of the function providing the input string "Hello, World!"`:
```python
print(flip_case("Hello, World!"))  # Output: "hELLO, wORLD!"
```

And here is an example usage of the function providing the input string "Flexibility is key.":
```python
print(flip_case("Flexibility is key."))  # Output: "FLEXIBILITY IS KEY."
``` 

This should output: "hELLO, wORLD!" for the first example and "FLEXIBILITY IS KEY." for the second example, as the characters have been flipped successfully.