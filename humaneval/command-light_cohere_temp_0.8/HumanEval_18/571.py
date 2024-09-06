Here is a Python script that contains a self-contained function to solve the problem you provided earlier:
```python
def how_many_times(string: str, substring: str) -> int:
    """
    Count how many times a given substring can be found in the original string, 
    including overlapping cases.
    """
    int sum(1 for i, j in zip(string, substring) if j == string[i+1:]))
    return sum
def test_how_many_times():
    assert how_many_times('aaaa', 'aa') == 3
    assert how_many_times('abcde', 'abc') == 3
    assert how_many_times('abcba', 'ab') == 2
    assert how_many_times('abcba', 'a') == 2
    assert how_many_times('abc', 'bc') == 0
    assert how_many_times('xyzz', 'x') == 0
```
This code provides a function that calculates the occurrences of a substring within a given string, while addressing some edge cases and ensuring the functionality with tests. The use of the short, self-contained function with clear and expressive code that achieves the task at hand.