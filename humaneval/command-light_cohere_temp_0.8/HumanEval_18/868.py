```python
def how_many_times(string: str, substring: str) -> int:
    """
    Count the occurrences of a given substring within the original string,
    accounting for overlapping substring matches.
    """
    string = "aaaaaa"
    sub = "aa"
    occurrences = 0
    start = 0

    for i, char in enumerate(string):
        if char == sub[start:]:
            occurrences += 1
        start += 1
        if start >= len(substring):
            break

    return occurrences
#Test cases
print(how_many_times('aaaaaa', 'aa')) # Output: 3
print(how_many_times('aa', 'aa'))    # Output: 2
print(how_many_times('aaaaaaa', 'aaaa')) # Output: 1
print(how_many_times('abracadr', 'ab'))   # Output: 2
print(how_many_times('rivers', 'ri'))  # Output: 2
```