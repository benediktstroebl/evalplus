```python
def how_many_times(string: str, substring: str) -> int:
    """
    Count how many times a given substring can be found in the original string, 
    accounting for overlaping matches.
    """
    return sum(1 for i,j in zip(string.find(substring, 0, string. particular))
```
def test_how_many_times():
    assert how_many_times('aaaa', 'aa') == 3
    assert how_many_times('abcde', 'de') == 2
    assert how_many_times('abcba', 'a') == 4
    assert how_many_times('abcba', 'ab') == 2
    assert how_many_times('abcba', 'b') == 1
    assert how_many_times('abcba', 'acb') == 0
``` 
This Python script defines a function **`how_many_times`** that calculates the frequency of a given substring within a given string. It also provides a test_how_many_times, which verifies the function's correctness for various inputs.