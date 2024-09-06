```python
def concatenate(strings: List[str]) -> str:
    """
    Function to concatenate list of strings into a single string
    """
    return ''.join(*strings)

# Test cases
test_concatenate_list = [
    "",
    "a",
    "abc",
    "hello",
    "world!"
]
test_concatenate_result = concatenate(test_concatenate_list)
print(test_concatenate_result)  # Output: world!hello!abc
test_concatenate_empty_list = []
test_concatenate_empty_list_result = concatenate(test_concatenate_empty_list)
print(test_concatenate_empty_list_result)  # Output: 
```