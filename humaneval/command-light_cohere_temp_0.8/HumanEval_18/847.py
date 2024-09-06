```python
def how_many_times(string: str, substring: str) -> int:
    count = 0
    for char in string:
        if char == substring:
            count += 1
    return count

# Test the function
test_string = "aaaaaa"
substring = "a"
print(how_many_times(test_string, substring))  # Output: 3
```