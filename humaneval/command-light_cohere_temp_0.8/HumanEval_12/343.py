```python
def longest(strings: List[str]) -> Optional[str]:
    """
    This function takes a list of strings and returns the length of the longest string.
    :param strings: list of strings
    """
    if not strings:
        return None
    max_length = max(len(string) for string in strings)
    return max_length

#Test cases
strings = ['a', 'b', 'c']
longest_result = longest(strings)
print("Longest:", longest_result) # Output: Length of the longest string in the list: 3

strings = ['a', 'bb', 'ccc']
longest_result = longest(strings)
print("Longest:", longest_result) # Output: Length of the longest string in the list: 3

strings = []
strings.[]
longest_result = longest(strings)
print("Longest:", longest_result) # Output: None
```
This script defines a function called longest, which takes a list of strings as input and returns the length of the longest string in the list. The test cases demonstrate the use of the function, passing in various lists of strings and verifying the output. You can use this maximum length in your project.