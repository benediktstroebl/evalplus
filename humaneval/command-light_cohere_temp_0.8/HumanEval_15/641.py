```python
def string_sequence(n: int) -> str:
    return f" {0:0>{n:02d} "

def test_sequence(test_num: int) -> None:
    assert str(test_sequence(test_num)) == f" {0:0>{test_num:02d} ",

    assert len(test_sequence(0)) == 1
    assert len(test_sequence(10)) == 1
    assert len(test_sequence(100)) == 1

    assert test_sequence(5) == '0 1 2 3 4 5'
    assert test_sequence(6) == '0 1 2 3 4 5'
    assert test_sequence(1000) == '0 1000 00 000'

# Usage:
test_sequence(0)
test_sequence(1)
test_sequence(5)
test_sequence(10)
test_sequence(15) # Should fail
```
The function `string_sequence` returns a string containing space-delimited numbers starting from 0 up to `n` (inclusive). It uses f- strings formatting to display the numbers in a formatted way.

The function is then tested with several inputs using the `test_sequence` function, which asserts that the output of `string_sequence` is correct for the given input. 

Finally, the function is called with some test inputs, and the results are printed to the console.