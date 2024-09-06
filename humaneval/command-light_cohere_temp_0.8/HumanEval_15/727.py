```python
def string_sequence(n: int) -> str:
    return f" {0:04d} ".format(n)

# tests
def test_string_sequence():
    assert string_sequence(0) == '0'
    assert string_sequence(1) == '01'
    assert string_sequence(5) == '0105'
    assert string_sequence(10) == '011010'
    assert string_sequence(100) == '010101010101'
    assert string_sequence(205) == '01010101010101'

if __name__ == "__main__":
    test_string_sequence()
```
This code defines a function `string_sequence` that returns a string containing a sequence of numbers starting from 0 up to `n` times, where `n` is passed as an argument. The function uses the `f-string formatting` to format the number as a four-digit string. The test_string_sequence function contains unit tests to ensure the correctness of the `string_sequence` function.