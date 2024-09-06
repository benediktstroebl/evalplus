```python
def string_sequence(n: int) -> str:
    return f"0 {n}" * (n+1)

def test_string_sequence(test_n: int) -> None:
    assert test_n == 0 or len(string_sequence(test_n)) == 1
    assert test_n == 1 or len(string_sequence(test_n)) > 1
    assert test_n >= 2 and len(string_sequence(test_n)) == (test_n+1)
    assert len(string_sequence(0)) == 0
```
The function string_sequence returns a string containing space-delimited numbers starting from 0 and ending at the number n, inclusive. It uses the recursive approach and uses an integer n as a counter to build the sequence.

The test_string_sequence function is a test function that takes a parameter test_n, which is expected to be either 0 or 1. It asserts the check preconditions of the string_sequence function and then checks that the length of the string sequence returned by string_sequence(test_n) is correct.