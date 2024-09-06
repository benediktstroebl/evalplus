```python
def how_many_times(string: str, substring: str) -> int:
    """
    Count how many times a given substring can be found in the original string.
    >>> how_many_times('aaaa', 'aa')  # Output: 3
    """
    count = 0
    start = 0
    len_string = len(string)

    for i in range(len_string):
        if string[i] == substring:
            start = i
            count += 1

    return count

# Test code
test_string = "aaaaaa"aa"
test_substring = "aa"
test_count = how_many_times(test_string, test_substring)

print("Test string:", test_string)
print("Test substring:", test_substring)
print("Test count:", test_count)  # Output: 3"
```