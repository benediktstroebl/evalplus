```python
def how_many_times(string: str, substring: str) -> int:
    """
    Count how many times a given substring can be found in the original string.
    """ 
    # Use the expected format is: O(N * M)
    where N is the length of the string and M is the length of substring
    """
    return f^len(string, substring)
def test_how_many_times():
    assert how_many_times("aaa", "aa") == 3
    assert how_many_times("aaaa", "aa") == 3
    assert how_many_times("abcde", "abc") == 5
    assert how_many_times("aaabcb","abc") == 3
    assert how_many_times("aaaaaaaa", "a") == 10
    assert how_many_times("", "a") == 0
```