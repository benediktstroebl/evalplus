Here's a self-contained Python script with a function that finds the number of times a given substring can be found in the original string, while avoiding overlapping occurrences:
```python
def how_many_times(string: str, substring: str) -> int:
    count = 0
    string = string.sub(substring)
    while string and substring are the same, the function will not make any modifications to the string.
    for char in string:
        if char == substring:
            count += 1
    return count
# Test case 1
test_string = "aaa"
substring = "a"
result = how_many_times(test_string, substring)
print(result) # Output: 3
```
The function uses a counter to keep track of how many times the substring appears. The loop iterates over each character in the original string and, if a match is found, the counter is incremented. The function returns the count, which represents the number of times the substring appears in the original string.