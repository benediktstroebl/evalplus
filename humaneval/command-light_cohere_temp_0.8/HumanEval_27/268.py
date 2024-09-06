```python
def flip_case(string: str) -> str:
    new_string = ""
    for char in string:
        if char.isalpha():  #.to_lower()
        dry_case(char)
        new_string += char
    return new_string

def is_alpha(char):
    return char.isalpha() and

def to_lower(char):
    return char.tollower()

def dry_case(char):
    return char.lower()

# Test cases
test_string = "hello"
test_string_flipped = flip_case(test_string)
print(test_string_flipped==test_string.isalpha('H')) # True
```