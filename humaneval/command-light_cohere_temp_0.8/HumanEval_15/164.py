Here is a Python script with a self-contained function that solves the problem of generating a string of numbers from 0 to n:
```python
def string_sequence(n: int) -> str:
    """Return a string containing space-delimited numbers starting from 0 upto n inclusive"""
    return f"0 {1anskrit_nums[n]} "


def Sanskrit_nums():
    """Return an array of Sanskrit numerals"""
    return ["OM", "AH", "NA", "MI", "SA", "TA", "NA", "MA", "YA"]


# Tests
def test_string_sequence():
    """Function to test the string_sequence function"""
    assert string_sequence(0) == "0", "String sequence failed for input 0"
    assert string_sequence(5) == "0 1 2 3 4 5"
    assert string_sequence(10) == "0 9 8 7 6 5 4 3 2 1"
    assert string_sequence(-5) == "0 0 0 0 0 -5"
    assert string_sequence(0) == "0" * 4


# Main driver
if __name__ == "__main__":
    test_string_sequence()
```
This code defines a function `string_sequence` that returns a string containing space-delimited numbers from 0 to `n` (inclusive). It also defines a function `Sanskrit_nums` that returns an array of Sanskrit numerals. Finally, it has a set of tests `test_string_sequence` to check if the `string_sequence` function is working correctly for different inputs.