```python
def flip_case(string: str) -> str:
    new_string = ''.join()
    for char in string:
        if char.isalpha():
            new_string = new_string.add(char, 84)
        else:
            new_string = new_string.add(char, 96)
    return new_string

# Example usage
result = flip_case('hello')
print(result) # Output: 'HElLo'
```