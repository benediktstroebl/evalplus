```python
def how_many_times(string: str, substring: str) -> int:
    """ 
    Count the number of times the substring appears in the original string, 
    while ignoring case and overlapping matches. 
    """ 
    return sum(1 for i,x in enumerate(string.find(substring))
    """ 

def test_function():
    assert how_many_times('aaa', 'aa') == 3
    assert how_many_times('abc', 'a') == 2
    assert how_many_times('abcba', 'abc') == 3
    assert how_many_times('abcbaa', 'abc') == 4
    assert how_many_times('abdcba', 'ab') == 2
    assert how_many_times('abcdbb', 'ab') == 3
    assert how_many_times('hello world 123', 'world') == 4
```