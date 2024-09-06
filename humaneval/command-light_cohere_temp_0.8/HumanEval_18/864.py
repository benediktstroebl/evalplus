```python
def how_many_times(string: str, substring: str) -> int:
    count = 0
    for char in substring:
        if char in string:
            count += 1
    return count

# Test the function
test_text = "aaaaaa"
test_substring = "a"
result = how_many_times(test_text, test_substring)
print("Result:", result)

# Test case 2
test_text = "This is a test"
test_substring = "ats"
result = how_many_times(test_text, test_substring)
print("Result:", result)
```