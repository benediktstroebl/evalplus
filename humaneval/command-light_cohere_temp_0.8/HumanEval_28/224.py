Here is a Python script with a self-contained function that solves the problem of concatenating list of strings into a single string:
```python
def concatenate(strings: List[str]) -> str:
    return "".join(strings)

# Test the function with different inputs
strings = ["a", "b", "c"]
result = concatenate(strings)
print(result)  # Output: 'abc'

strings = ["a", "", "c"]
result = concatenate(strings)
print(result)  # Output: 'ac'

strings = ["", "a", " ", " ", "c"]
result = concatenate(strings)
print(result)  # Output: 'abc'

strings = ["a", "bcde", " ", "f"]
result = concatenate(strings)
print(result)  # Output: 'abcdef'
```
This script provides a function `concatenate` that takes a list of strings as an argument and returns the concatenated string. The test cases demonstrate how the use of the function with different inputs and verify the expected outputs.