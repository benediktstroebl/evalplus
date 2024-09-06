Here's a self-contained Python function that calculates the length of any given string:
```python
def strlen(string: str) -> int:
    return len(string)

# Test cases
print(strlen(''))
print(strlen(''))  

print(strlen('abc'))
print(strlen('ABC'))
print(strlen('abcde'))
```
This code defines a function `strlen` that calculates the length of the given string using the `len()` function. The function returns the `len(string)` where `string` is the parameter passed to the function. The test cases provided validate the strings with empty content, single characters, and multiple characters.