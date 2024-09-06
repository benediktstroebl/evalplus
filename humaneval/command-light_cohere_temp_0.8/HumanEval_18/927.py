Here is a self-contained Python script that includes a function that solves the problem you have described:

```python
def how_many_times(string: str, substring: str) -> int:
    count = 0
    for char in substring:
        if char in string:
            count += 1
    return count

# Test the function
test_string = "aaaaaa"
test_substring = "a"
result = how_many_times(test_string, test_substring)
assert result == 3
```
This script defines a function how_many_times that takes two arguments: a string and a substring. The function then uses a loop to iterate over each character in the substring and counts how many times it finds a match in the original string. The function returns the goal of finding the number of occurrences of the substring.