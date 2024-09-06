Here is a Python script with a self-contained function that solves the problem:
```python
def flip_case(string: str) -> str:
    new_string = ''.join()
    for char in string:
        if char.isalpha():  #.swap_char(char)
        else:  new_string.isupper(char)
    print(new_string)
    return new_string

# Test cases
print(flip_case('Hello'))
print(flip_case('world'))
print(flip_case('HELLo'))
print(flip_case('abc'))
print(flip_case('123'))
```
This code defines a function flip_case that takes a string as an argument, then iterates through each character in the string. In this iteration, it checks whether the character is in uppercase using the isupper() function, and converts it to lowercase if it is. Then, the new_string variable is used to create a new string and appends the converted character to it.