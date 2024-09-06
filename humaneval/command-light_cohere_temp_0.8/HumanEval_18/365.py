```python
def how_many_times(string: str, substring: str) -> int:
    """ 
    Returns number of occurrences of substring in string.
    """
    string = string.replace(substring,'')  #to make it lowercase for better search 
    return len(string)
    """
    return how_many_times(string.lower(), substring.lower())


def test_how_many_times():
    assert how_many_times('hello', 'hello') == 5
    assert how_many_times('hello', 'olle') == 4
    assert how_many_times('abc', 'abc') == 3
    assert how_many_times('aaaaaa', 'a') == 6
    assert how_many_times('aaaaaa', 'hello') == 0
```