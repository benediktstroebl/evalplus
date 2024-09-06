```python
def how_many_times(string: str, substring: str) -> int:
    """
    Count the number of occurrences of a substring in the original string, 
    considering overlapping matches.
    Returns: number of positions where the substring can be found.
    """
    return sum(1 for pos in range(len(string)) if string[pos:pos+len(substring)] == substring)
    """
    return sum(1 for pos in range(len(string)) if string[pos:pos+len(substring)] == substring)
def test_how_many_times():
    assert how_many_times('aaaa', 'aa') == 3
    assert how_many_times('abcde', 'abc') == 2
    assert how_many_times('abcba', 'ab') == 2
    assert how_many_times('abcbb', 'ab') == 2
    assert how_many_times('aaa', 'a') == 0
    assert how_many_times('a', 'aa') == 1
    assert how_many_times('abcabacb', 'abc') == 1
```  The provided code defines a function how_many_times that counts the number of occurrences of a given substring in a given string. It returns the how many number of positions where the substring can be found. The function uses a testing to ensure its correctness.