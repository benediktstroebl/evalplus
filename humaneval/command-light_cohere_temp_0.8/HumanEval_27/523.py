```python
def flip_case(string: str) -> str:
    return ''.join(c if c.isalpha() else upper() else c.isupper()

    return string.

x = "hello"
y = flip_case(x)
print(x) # HELLO
print(y) # HELLo
 ```