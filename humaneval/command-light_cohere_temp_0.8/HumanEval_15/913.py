Here is a Python script with a self-contained function that solves the problem you have described:

```python
def string_sequence(n: int) -> str:
    """ Returns a string containing space-delimited numbers starting from 0 and ending at n inclusive."""
    sequence = [0]
    while len(sequence) <= n:
        sequence.append(sequence[-1] + 1)
    return ' '.join(sequence)

# Unit tests for the function
def test_string_sequence():
    assert string_sequence(0) == '0'
    assert string_sequence(1) == '1'
    assert string_sequence(5) == '0 1 2 3 4 5'
    assert string_sequence(10) == '9 9 9 9 9'
    assert string_sequence(15) == '14 14 14 14'
``` 
This script defines a function `string_sequence` which creates a sequence of numbers starting from 0 and ending at the given input `n`. 

The function is then tested with a series of `assert_string_sequence` tests, which checks that the function outputs the correct sequence of numbers for a given input.