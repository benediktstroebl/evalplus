Here is a self-contained Python function that calculates the length of any given string:
```python
def strlen(string: str) -> int:
    return len(string)

# Test cases for strlen function
string1 = ''
string2 = 'abc'
string3 = 'hello world'

print(strlen(string1))  # Output: 0
print(strlen(string2))  # Output: 3
print(strlen(string3))  # Output: 11
```
This script defines a function `strlen` that takes a string as an argument and returns its length. The function uses the regular expression `len` to get the length of the string. The test cases show that the `strlen` function correctly calculates the length of each given string.