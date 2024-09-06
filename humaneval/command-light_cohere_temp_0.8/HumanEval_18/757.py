```python
def how_many_times(string: str, substring: str) -> int:
    """
    Count the number of occurrences of a given substring within the original string, accounting for case-sensitive matches and ignoring punctuation and capitalization.
    Returns the how number of times the substring appears in the string.
    """
    note on: string.string match, case-sensitive
    i.e., the string.match and case match.

def test():
    string = "hello world"
    sub = "o"
    return how_many_times(string, sub) == 3
```