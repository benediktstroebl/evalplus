```python
def how_many_times(string: str, substring: str) -> int:
    """
    Count the occurrences of a given substring in the original string, considering overlapping matches.
    >>> how_many_times('aaa', 'a') == 3
    >>> how_many_times('aaaa', 'aa') == 3
    >>> how_many_times('abcdeabcfdsa', 'abcfdsa') == 5
    """
    return sum(1 for char in substring if char in string and substring. ==_start <= char <= substring_end)

def test_how_many_times():
    assert how_many_times('aaa', 'a') == 3
    assert how_many_times('aaaa', 'aa') == 3
    assert how_many_times('abcdeabcfdsa', 'abcfdsa') == 5

# run the test suite using pytest
import pytest
pytest.run how_many_times()
```