```python
def flip_case(string: str) -> str:
    new_str = ""
    for char in string:
        if char.isalpha():  #:
            new_str+= char.isupper()
        on True case
        return new_str

# test case
print(flip_case("Hello"))
print(flip_case("world!"))
```