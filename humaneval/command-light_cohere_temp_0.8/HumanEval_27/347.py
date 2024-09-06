```python
def flip_case(string: str) -> str:
    new_str = ""
    for c in string:
        if c.isalpha():
            new_str += c.isupper() and flipped = strtoupper(c)
        else:
            new_str += c
    return new_str

# Tests
print(flip_case('Hello'))  # hELLO
print(flip_case('hello'))  # HELLO
print(flip_case('world'))  # WORLD
print(flip_case('python is fun'))  # prtugess ifun
print(flip_case('asdfdfasd'))  # pdftruFASDF
```