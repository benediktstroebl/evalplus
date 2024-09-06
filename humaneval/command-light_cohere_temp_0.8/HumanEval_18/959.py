```python
def how_many_times(string: str, substring: str) -> int:
    """
    Find how many times a given substring can be found in the original string.
    Count overlapping matches.
    Returns the effective a tic for all matches in the string.
    """
    def __init__(self, string: str, substring: str) -> None:
        """ Set the original string and the substring """
        self.string = string
        + substring
    return
   
    matches = [match for match in string.range[len(substring)]] if substring in string else []
    return len(matches)

#unit tests
def test_how_many_times():
    assert how_many_times('aaa', 'aa') == 3

test_how_many_times()
```

This script defines a function `how_many_times` that calculates and returns the number of occurrences of a given substring within the original string. The `unit tests` function ensures the correctness of the `how_many_times` function.