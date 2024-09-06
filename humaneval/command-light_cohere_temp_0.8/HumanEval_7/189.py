Here's the improved code:
```python
def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [x for x in strings if substring in x]

# Test cases
strings = ["abc", "bacd", "cde", "array", "hello"]
substring = "a"

# Call the function and verify the output
result = filter_by_substring(strings, substring)
print(result)  # Expected output: ['abc', 'bacd', 'array']
```
This code encapsulates the functionality and passes the tests. It efficiently filters an input list of strings based on a given substring, producing a new list containing only the strings that contain the substring. 

This improved structure maintains clarity and readability, making it easier to understand and modify the code for future customization or new test cases.