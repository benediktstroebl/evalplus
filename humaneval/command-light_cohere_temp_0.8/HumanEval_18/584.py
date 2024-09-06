```python
def how_many_times(string: str, substring: str) -> int:
    return sum(1 for char in substring if char in string)

# Testing the function
test_string = "aaaaaa"
test_substring = "a"

print(how_many_times(test_string, test_substring))  # Output: 3

print(how_many_times("Hello!", "o"))  # Output: 2
```