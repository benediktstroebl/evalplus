```python
def how_many_times(string: str, substring: str) -> int:
    count = 0
    n = len(string)
    m = len(substring)
    for i in range(n):
        if string[i] == substring:
            count += 1
    return count

# Test the function
test_string = "aaaaaa"
test_substring = "aa"
result = how_many_times(test_string, test_substring)
print("Result:", result)

# Test with overlapping substring
test_string = "aaaaaaa"
test_substring = "aa"
result = how_many_times(test_string, test_substring)
print("Result:", result)
```