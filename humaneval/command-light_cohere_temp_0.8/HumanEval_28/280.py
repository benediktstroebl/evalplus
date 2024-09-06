Here's a self-contained Python function that concatenates lists of strings into a single string:
```python
def concatenate(strings: List[str]) -> str:
    return ''.join(strings)

# Example usage:
strings = ['a', 'b', 'c']
result = concatenate(strings)
print(result) # Output: 'abc'
```
This function takes a list of strings as input and returns a single string by concatenating all the strings together. The example usage provided also demonstrates how to use the function with a sample input.