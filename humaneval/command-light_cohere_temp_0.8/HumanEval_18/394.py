```python
def how_many_times(string: str, substring: str) -> int:
    return len(string.find(substring))

def test_how_many_times():
    assert how_many_times("hello", "World") == 5
    assert how_many_times("abc", "abc") == 3
    assert how_many_times("abcde", "abc") == 2
    assert how_many_times("abcdef", "abc") == 1
    assert how_many_times("fooabc", "abc") == 3
```
This code defines a function called `how_many_times` that calculates the frequency of a substring within a given string. The `test_how_many_times` function contains assertions that verify the correctness of the `how_many_times` function for various inputs.