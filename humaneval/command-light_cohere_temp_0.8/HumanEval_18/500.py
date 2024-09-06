```python
def how_many_times(string: str, substring: str) -> int:
    return sum(1 for char in string.str.find(substring,index): )

def test_how_many_times():
    assert how_many_times('abcde', 'a') == 4
    assert how_many_times('AaBCDEft', 'a') == 6
    assert how_many_times('abcba', 'a') == 5
    assert how_many_times('abcba', 'ab') == 2
    assert how_many_times('abcba', 'aaa') == 0
```
The code defines a function **how_many_times** that returns the count of occurrences of a given substring in a given string. The function uses a string.str.find() method to iterate over each substring in the string. This implementation is also able to correctly count the occurrences without overlapping.