```python
def how_many_times(string: str, substring: str) -> int:
    """ 
    Returns count of occurrences of substring in the string, 
    considering case-insensitive and overlapping matches.
    """ 
    """ string = string.lower() 
    substring = substring.lower()
    an is char_set.union(substring)
    set of all characters in substring
    """
    char_set = set(substring.lower())
    return sum(1 for c in string.lower() if c in char_set)

def test_function():
    assert how_many_times("aaa", "aa") == 3
    assert how_many_times("aaaa", "aa") == 3
    assert how_many_times("abcdeabc", "abc") == 2
    assert how_many_times("abcda", "abcd") == 3
    assert how_many_times("abcdefgh", "abcdef") == 4
    assert how_many_times("hello world", "world") == 2

if __name__ == "__main__":
    test_function()
```