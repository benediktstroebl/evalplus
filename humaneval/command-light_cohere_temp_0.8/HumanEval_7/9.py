Here's the solution to the problem using Python:

```python
def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [x for x in strings if substring in x]

# Test cases
strings = ["abc", "bacd", "cde", "array", "hello"]
substring = "a"

# Function call
result = filter_by_substring(strings, substring)

# Print results
print(result)  # Output: ['abc', 'bacd', 'array']
```

The function `filter_by_substring` takes a list of strings and a substring as input and returns a new list containing only the strings that contain the given substring. The function uses a list comprehension to filter the strings based on the presence of the substring.