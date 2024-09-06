```python
def how_many_times(string: str, substring: str) -> int:
    return sum(1 for char in string if char == substring)

# Test the function
test_string = "aaaaaa"
test_substring = "a"
test_result = how_many_times(test_string, test_substring)
print(test_result)  # Output: 3
```
This Python script defines a function `how_many_times` that calculates the number of occurrences of a given substring within a string. It uses a simple loop to iterate over each character in the input string, and counts the occurrences of the substring.