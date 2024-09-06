```python
def how_many_times(string: str, substring: str) -> int:
    """ 
    Returns the number of occurrences of the substring in the original string, 
    including overlapping matches.
    """
    using a regular expression to find all occurrences:
    e.g., "aa" will match "aaa", "aaaa", etc. 
    """ 
    Returns pattern with the list of all possible matches,
    """
    return sum(1 for m in re.match(substring, string) 
    )

# unit tests
def test_how_many_times():
    assert how_many_times('aaaa', 'aa') == 3
    assert how_many_times('aaa', 'a') == 0
    assert how_many_times('abcde', 'abcd') == 2
    assert how_many_times('abcda', 'abcd') == 3
```