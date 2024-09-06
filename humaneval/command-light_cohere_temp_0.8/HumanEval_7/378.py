Here is a self-contained Python script that solves the problem of filtering strings that contain a given substring:
```python
def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [x for x in strings if substring in x]

# Test cases
strings = ["abc", "bacd", "cde", "array", "hello world"]
substring = "a"

result = filter_by_substring(strings, substring)
print(result)  # Output: ['abc', 'bacd', 'array']
```

This script defines a function called `filter_by_substring` that takes a list of strings and a substring as input and returns a new list of strings that contain the given substring. The function uses a list comprehension to achieve this. 

The test cases demonstrate how the function works with different inputs.