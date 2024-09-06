```python
def how_many_times(string: str, substring: str) -> int:
    """
    Count how many times a given substring can be found in the original string while not overlapping.
    """
    string = string.replace(substring, string)
    count = 0
    start = 0
    for i, char in enumerate(string):
        if char == substring[start]:
            start += 1
        if start == len(substring):
            count += 1
    return count

# Test the function
text = "aaaaaaa"
substring = "aa"
result = how_many_times(text, substring)
print(result) # Output: 3
```