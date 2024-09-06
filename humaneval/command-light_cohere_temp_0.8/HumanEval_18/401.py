```python
def how_many_times(string: str, substring: str) -> int:
    """
    Count how many times a given substring can be found in the original string,
    while avoiding overlapping matches.
    """
    string: str
    substring: str
    counts = [0] * (len(substring) + 1)
    for i, char in enumerate(string):
        if char == substring[counts[i]]:
            counts[i+1] += 1
    return counts[-1]

# Test the function
test_string = "aaaaaa"aa"
test_substring = "aa"
test_count = how_many_times(test_string, test_substring)
print("Test string:", test_string)
print("Test substring:", test_substring)
print("Test count:", test_count)
```