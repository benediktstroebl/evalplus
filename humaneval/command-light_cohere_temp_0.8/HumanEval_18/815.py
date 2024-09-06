```python
def how_many_times(string: str, substring: str) -> int:
    return sum(1 for char in string if char == substring)
    
# Test the function
test_string = "aaaaaa"
test_substring = "a"
print(how_many_times(test_string, test_substring))  # Output: 3
```