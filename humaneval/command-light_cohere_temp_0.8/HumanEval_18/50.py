```python
def how_many_times(string: str, substring: str) -> int:
    """ 
    Returns the number of times the substring can be found in the original string.
    """ 
    return sum(1 for x in string.find(substring, 0, string. how(substring)) 
    """ 

def test_function():
    assert how_many_times("aaa", "a") == 3
    assert how_many_times("aaaa", "aa") == 3
    assert how_many_times("aaaaaaa", "aaaa") == 0
```