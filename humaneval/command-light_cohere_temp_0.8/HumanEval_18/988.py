Here is a Python script with a self-contained function that solves the problem:
```python
def how_many_times(string: str, substring: str) -> int:
    count = 0
    for i in string:
        if i == substring:
            count += 1
    return count

# Test the function
test_string = "aaaaaa"
test_substring = "a"
result = how_many_times(test_string, test_substring)
print("Result:", result)
```
This script defines a function `how_many_times` that takes two parameters: a string and a substring. It then iterates over the isn't the same as the string and counts the number of times the substring appears in the string. This function can be used to test itself using the test string and substring.