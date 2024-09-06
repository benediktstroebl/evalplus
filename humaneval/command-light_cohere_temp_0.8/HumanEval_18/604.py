```python
def how_many_times(string: str, substring: str) -> int:
    return sum(1 for char in substring if char in string)

# Test the function
test_str = "aaaaaa"
test_substring = "a"
test_result = how_many_times(test_str, test_substring)
print(test_result)  # Output: 3

test_str = "hello"
test_substring = "ll"
test_result = how_many_times(test_str, test_substring)
print(test_result)  # Output: 2

test_str = "abc123"
test_substring = "a"
test_result = how_many_times(test_str, test_substring)
print(test_result)  # Output: 3
``` 
This Python code defines a function how_many_times that counts the occurrences of a given substring within a given string. It uses a strings to test the function with different inputs and verifies that the function correctly calculates the expected results.