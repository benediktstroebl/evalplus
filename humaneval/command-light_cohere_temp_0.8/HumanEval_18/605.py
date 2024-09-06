```python
def how_many_times(string: str, substring: str) -> int:
    """
    Count the number of occurrences of a substring in the original string, 
    considering overlapping occurrences.
    """
    using a Python's slice notation and itertools.
    return sum(1 for i,j in enumerate(string.find(substring)))
    """

def test_how_many_times():
    assert how_many_times('aaa', 'aa') == 3
    assert how_many_times('aaaa', 'a') == 3
    assert how_many_times('abcde', 'de') == 2
    assert how_many_times('abcbaacccb', 'a') == 4
    assert how_many_times('iii', 'i') == 4
    assert how_many_times(' '', ' ') == 0
    assert how_many_times('  ', ' ') == 1
```
The above code defines a function called **`how_many_times`** that finds and counts the occurrences of a given substring in a given string. It also comes with a function to test its correctness with a set of test cases.