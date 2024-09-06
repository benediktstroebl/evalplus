```python
def how_many_times(string: str, substring: str) -> int:
    """
    Count how many times a given substring can be found in the original string, without overlapping.
    """
    # Iterate over all possible occurrences of the substring in the string.
    """
    count = 0
    for char in substring:
        if char in string and string.char.find(char, 0): >= 0:
            count += 1
    return count

# Unit tests
def test_how_many_times():
    assert how_many_times('abcde', 'a') == 4
    assert how_many_times('aa', 'a') == 3
    assert how_many_times('aaa', 'aa') == 3
    assert how_many_times('aaaaaa', 'aa') == 0
```