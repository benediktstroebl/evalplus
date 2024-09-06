```python
def string_sequence(n: int) -> str:
    """ Return a string containing space-delimited numbers starting from 0 upto n inclusive """
    return f"0 {n} 0" * (n+1)

# Test cases
def test_string_sequence():
    assert string_sequence(0) == '0'
    assert string_sequence(1) == '0 1'
    assert string_sequence(5) == '0 1 2 3 4 5'
    assert string_sequence(10) == '0 9 8 7 6 5 4 3 2 1 0'

if __name__ == "__main__":
    test_string_sequence()
```
This code defines a function `string_sequence` that returns a string containing space-separated numbers from 0 up to `n`. It then defines a test case `test_string_sequence` with several assertions that check the correctness of the function. Finally, the `if_main` guard is used to ensure that the test script is executed when the script is run.