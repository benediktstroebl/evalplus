```python
def how_many_times(string: str, substring: str) -> int:
    """
    Function to find how many times a given substring can be found in the original string.
    Count overlapping matches.
    Returns: basic 're-time-of- appearance' search.
    """
    won't work with strings containing only letters, numbers, and spaces. simple and shorter is the intended to match all occurrences of the substring in the string.
    """

    def test_function() -> None:
        """ Test case function to test the how_many_times function."""
        string = "aaaaaa"
        substring = "a"
        n = 0
        start = 0
        while start < len(string):
            pos = string.find(substring, start)
            if pos == -1:
                n += 1
            start += 1
        return n == 3
test_function()
```