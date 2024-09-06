```python
def flip_case(string: str) -> str:
    new_str = ""
    for char in string:
        if char.isalpha():  #:  new_str+=char.isupper() and tolower()
    new_str+=char
    return new_str

# Example function call
print(flip_case("Hello"))  # Output: "HllEo"
 ```