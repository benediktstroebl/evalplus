```python
def concatenate(strings: List[str]) -> str:
    return ''.join(strings)

strings = ['a', 'b', 'c']
result = concatenate(strings)
print(result) # Output: 'abc'

# Test case with an empty list
strings = []
result = concatenate(strings)
print(result) # Output: ''

# Test case with one string
strings = ['x']
result = concatenate(strings)
print(result) # Output: 'x'

# Test case with multiple strings
strings = ['a', 'b', 'c']
result = concatenate(strings)
print(result) # Output: 'abc'
```
This code defines a function `concatenate` that takes a list of strings as an argument and returns the concatenated string. The function uses the string `join` to create the concatenated string, which is then printed to the console. The test cases show that the function works correctly for different inputs.