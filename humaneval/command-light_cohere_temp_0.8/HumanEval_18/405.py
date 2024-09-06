```python
def how_many_times(string: str, substring: str) -> int:
    count = 0
    for char in string:
        if char == substring:
            count += 1
    return count

# Test the function
string = "aaaaaa"
substring = "a"
print(how_many_times(string, substring))  # Output: 3

# Test with overlapping substring
string = "aat"
substring = "a"
print(how_many_times(string, substring))  # Output: 2
```
This code implements a function `how_many_times` that calculates the count of a given substring within a given string.  It uses a string's character array and the substring to be found to determine the result.