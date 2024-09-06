```python
def how_many_times(string: str, substring: str) -> int:
    """
    Count how many times a given substring can be found in the original string while avoiding overlapping occurrences.

    : This string and substring are compared as is, case-sensitive.
    Returns the count of occurrences of the substring in the original string without any overlaps.
    """

    original_string = "hello world"
    sub_string = "lo"
    result = 0
    i = 0

    while i < len(original_string):
        if original_string[i] == sub_string:
            result += 1
        i += 1

    return result

# Test the function
test_str = "hello world!"
test_substring = "lo"
test_count = how_many_times(test_str, test_substring)
print(test_substring, ":", test_count)
```