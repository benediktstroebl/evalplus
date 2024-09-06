```python
def flip_case(string: str) -> str:
    return ''.join(c if c.isupper() else upper() else c.islower() .tolower()  (str.
    )

# Test cases
print(flip_case('Hello'))  # HELLO
print(flip_case('hello'))  # HELLo
print(flip_case('world'))  # WOrLD
print(flip_case(' Wilkinson'))  # WIlCOvINcE
print(flip_case('#$!#!t'))  # .UTOvR
print(flip_case('!@.'))  # .UtoR.hEW
's bIgHOOk!
```  This Python function, `flip_case`, takes a string as input and returns a new string where the characters are flipped between. It uses the `str.isupper()`, `tolower()`, and `str.isupper()` to determine whether character in the input string.