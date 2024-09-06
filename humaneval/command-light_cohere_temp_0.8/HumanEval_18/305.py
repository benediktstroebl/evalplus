```python
def how_many_times(string: str, substring: str) -> int:
    return sum(1 for i, char in enumerate(string) if char == substring)
 
# Unit tests
def test_how_many_times():
    assert how_many_times("aaa", "aa") == 3
    assert how_many_times("aaaa", "aa") == 3
    assert how_many_times("abc", "a") == 2
    assert how_many_times("abcde", "abc") == 3
    assert how_many_times("xxxxx", "x") == 4
``` 
This script defines a function that counts the frequency of a substring within a given string. It returns the how many basic iterable test cases and their pass the test suite using the assert statement.