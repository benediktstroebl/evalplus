```python
def flip_case(string: str) -> str:
    return ''.join(c if c.isupper() else((ord(c)-1, 95) else (ord(c)-65)) for c in string)

# Test cases
print(flip_case('hello'))      # HELLO
print(flip_case('world'))     # WODRL
print(flip_case('isUPPER'))   # cisUPRER
print(flip_case('lower'))   # lOWERER
print(flip_case('UPPER'))    # upPER
```