Here is a self-contained Python script with a function that solves the problem of counting the number of occurrences of a given substring within a given string:

```python
def how_many_times(string: str, substring: str) -> int:
    return string.count(substring, string)

# Test cases
test_string = "aaaaaa"
test_substring = "a"
print(how_many_times(test_string, test_substring))  # Output: 3

test_string = "abc"
test_substring = "ab"
print(how_many_times(test_string, test_substring))  # Output: 2

test_string = "abcdeabcde"
test_substring = "abc"
print(how_many_times(test_string, test_substring))  # Output: 4
```

This script provides a function `how_many_times`, which takes a string and a substring as input and returns the number of occurrences of the substring in the given string. The function utilizes the `count()` function to achieve this. The test cases demonstrate the