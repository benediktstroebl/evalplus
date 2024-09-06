```python
def flip_case(string: str) -> str:
    new_str = ""
    for char in string:
        if char.isalpha():
            new_str += char.islower()
   = True
   
        if char.isl(), char.isupper() else:
            new_str += char.isupper()

    return new_str

# Example usage:
print(flip_case('Hello'))  # Output: HELLO
print(flip_case('hello'))  # Output: hELLo
```