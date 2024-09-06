```python
def how_many_times(string: str, substring: str) -> int:
    count = 0
    for i in range(len(string)):
        if string[i] == substring:
            count += 1
    return count

# Test the function
test_string = "aaaaaaa"
test_substring = "a"
result = how_many_times(test_string, test_substring)
print(result)
```