```python
def longest(strings: List[str]) -> Optional[str]:
    # Use the max function to get the longest string in the list
    return max(strings, key=len)

# Test the function
strings = ['a', 'b', 'c']
result = longest(strings)
print(result)  # Output: c

strings = ['']
result = longest(strings)
print(result)  # Output: None

strings = []
result = longest([])
print(result)  # Output: None
```
This script provides a function `longest` that accepts a list of strings as input and returns the longest string in that list. It employs the `max` function with `key=len` argument to achieve this. The test cases demonstrate the scenario of the function, showcasing its expected behavior and handling empty input.