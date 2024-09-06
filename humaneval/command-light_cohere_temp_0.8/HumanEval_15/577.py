```python
def string_sequence(n: int) -> str:
    """ Returns a string containing space-delimited numbers starting from 0 and ending at n inclusive"""
    return f" {*(0, )[n]} "  # Uses Python's expand format specifier which repeats the arguments n number of times starting from 0

tests = [
    """
    def test_string_sequence():
        assert string_sequence(0) == '0'
        assert string_sequence(5) == '0 1 2 3 4 5'
        assert string_sequence(10) == '0 9 8 7 6 5 4 3 2 1'
        assert string_sequence(15) == '0 14 13 12 11 10 9 8 7 6 5 3'
    """
```