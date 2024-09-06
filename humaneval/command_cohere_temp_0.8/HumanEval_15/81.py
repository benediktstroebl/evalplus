```python
def string_sequence(n):
    """ Return a string containing space-delimited numbers starting from 0 up to including n.
    """
    return ' '.join(map(str, range(n+1)))

# Tests
import pytest

def test_string_sequence():
    assert string_sequence(0) == '0'
    assert string_sequence(5) == '0 1 2 3 4 5'
    assert string_sequence(10) == '0 1 2 3 4 5 6 7 8 9 10'

```
The above code uses the `range()` function to generate a list of numbers from `0` up to `n` and then uses `str` to convert these numbers into strings. Finally, the `join()` method is used to concatenate these strings into one string with spaces as separators.