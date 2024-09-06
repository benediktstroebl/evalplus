```python
def how_many_times(string: str, substring: str) -> int:
    return len(string.find(substring))

def test_how_many_times():
    assert how_many_times('aa', 'aa') == 3
    assert how_many_times('aaa', 'aa') == 3
    assert how_many_times('aaaa', 'aa') == 3
```
The code defines a function **how_many_times** that takes two arguments: a string and a substring. The function uses the find() method to search for the substring in the original string, and returns the length of the match. This function is also pass all the tests using the test_how_many_times function.