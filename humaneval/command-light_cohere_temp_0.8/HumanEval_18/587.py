```python
def how_many_times(string: str, substring: str) -> int:
    """
    Count the number of occurrences of a substring in the original string.
    Using overlapping matches are:
    substring can be contained in the original string.
    """
    if not string:
        return 0
    if not substring:
        return len(string)
    return 1 + how_many_times(substring, string[string.substring(substring))

# Test case: 
print(f'Overlapping matches: { how_many_times("aaaa", "aa") }) 
# Expected Output: 3

```