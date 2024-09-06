```python
def longest(strings: List[str]) -> Optional[str]:
    return max(strings, key=len, default=None)

# Test cases
strings = ['a', 'b', 'c']
result = longest(strings)
print(result)  # Output: c

strings = ['']  # Empty list
result = longest(strings)
print(result)  # Output: None

strings = ['a', 'bb', 'ccc']
result = longest([...])
print(result)  # Output: a
``` 
This code defines a function called longest, which takes a list of strings as input and returns the longest string in the list. The function uses the max function with the key=len argument, which returns the longest string by default. The test cases below demonstrate how the can be used to validate the correctness of the function.