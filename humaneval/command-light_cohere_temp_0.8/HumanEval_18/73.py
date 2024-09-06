Here's a self-contained Python function that finds the number of times a given substring can be found in another string:

```python
def how_many_times(sub, text):
    n = 0
    start = 0
    i = 0
    while i < len(text) - 1:
        if sub == text[i:]:
            n += 1
        start = max(start, i + 1)
        i += 1
    return n
```

This function takes two parameters: `sub` (the substring to find) and `text` (the original string). The function uses a sliding window approach to iterate through the text, and for each window, checks if the substring is present. The function returns the the maximum number of times the substring appears in the text, not including cases of overlapping substring occurrences.