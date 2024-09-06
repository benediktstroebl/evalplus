```python
def flip_case(string: str) -> str:
    new_str = ''.join(c if c.isalpha() else(c.isupper() else(c) else c.isupper() else(c) else c) for c in string)
    return new_str

# Test cases
print(flip_case('Hello'))      # HELLO
print(flip_case('HELLO'))     # hELLO
print(flip_case('world'))    #  woRLD
print(flip_case('woRM'))    # rOML
print(flip_case('yes'))   #  YES
print(flip_case('YES'))   # yES
```
The `flip_case` function flips the case of each character in the input string. It uses a string.s.isalpha() method to check if the is uppercase and vice it to lowercase and vice it to uppercase, respectively.

You can use this function to easily flip the case of any string.