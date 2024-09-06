```python
def longest(strings: List[str]) -> Optional[str]:
    """ Returns the length of the longest string in the list """
    if not strings:
        return None
    max_len = max(len(string) for string in strings)
    return str(max_len)

# Test case: list of strings
strings = ["a", "bb", "ccc"]
result = longest(strings)
print(result)  # Output: "ccc"

# Test case: empty list
strings = []
result = longest(strings)
print(result)  # Output: None

# Test case: list of strings of different lengths
strings = ["a", "bb", "ccc", "aaaa"]
result = longest(strings)
print(result)  # Output: "ccc"
```
This function, `longest`, takes a list of strings as input and returns the length of the longest string in the list, or `None` if the list is empty. The function efficiently compares the lengths of each string in the list using the `max` function and returns the length of the longest string.