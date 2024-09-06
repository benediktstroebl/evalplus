```python
def how_many_times(string: str, substring: str) -> int:
    """
    Counts how many times a given substring can be found in the original string, 
    considering cases where the substring is contained zero or more times.

    :Returns the how many times the string contains the substring.
    """
    count = 0
    for i in range(len(string)):
        if string[i] == substring:
            count += 1
    return count

# Example usage:
text = "aaaabbbb"
substr = "ab"
print(how_many_times(text, subtext))  # Output: 3
```