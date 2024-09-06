Here's a Python script that demonstrates the functionality of the provided function `how_many_times`:
```python
def how_many_times(string: str, substring: str) -> int:
    """
    Count how many times a given substring can be found in the original string.

    : Overlapping is strings are treated as different occurrences.

    Args: 
        string: The original string
        substring: The substring to search

    Returns: 
        int: Number of times the substring is found
    """
    return sum(1 for x in string.search(substring, 0, len(substring)))

# Test the function
test_str = "aaaaaaa"
sub_str = "aa"

print(how_many_times(test_str, sub_str))  # Output: 6
```