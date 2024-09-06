```python
def how_many_times(string: str, substring: str) -> int:
    """
    Count the number of occurrences of a given substring within the original string,
    handling overlapping occurrences.
    """
    def _recursively_count(text, pattern):
        count = 0
        i, j = 0, 0
        while i < len(text) or j >= 0:
            if text[i] == pattern[j]:
                count += 1
                i += 1
                j -= 1
            elif j == len(pattern) - 1:
                count += 1
                i += 1
            else:
                j += 1
        return count

    string = "aaaaaa"
    substring = "a"
    return _recursively_count(string, substring)

def _recursively_count(text, pattern):
    if not pattern: return 0
    if len(pattern) == 1 and pattern[0] in text: return _recursively_count(text, pattern[0]) + 1
    count = how_many_times(text, pattern)
    for i in range(len(pattern) - 1):
        count += _recursively_count(text, pattern[i+1:])
    return count
```