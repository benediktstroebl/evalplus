```python
def how_many_times(string: str, substring: str) -> int:
    """ 
    Count how many times a given substring can be found in the original string while avoiding overlapping. 
    Args: 
        string: The input string 
        substring: The substring to search in the string 
    Returns: 
        int: Number of occurrences of the substring 
    """
    return sum(1 for s in string.find(substring, 0, len(substring) == len(string))
def test_how_many_times():
    assert how_many_times('aaa', 'aa') == 3
    assert how_many_times('aaaa', 'aa') == 3
    assert how_many_times('abcde', 'abc') == 2
    assert how_many_times(' sunburn ', ' sun') == 0
```