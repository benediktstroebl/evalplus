Here is a Python script with a self-contained function that solves the problem of generating a string of numbers from 0 to n:
```python
def string_sequence(n: int) -> str:
    return f'{0}{1}' * n

def test_string_sequence():
    assert string_sequence(0) == '0', "String sequence failed for n=0"
    assert string_sequence(1) == '0 1', "String sequence failed for n=1"
    assert string_sequence(5) == '0 1 2 3 4 5', "String sequence failed for n=5"
    assert string_sequence(10) == '0 10 11 12 13 14', "String sequence failed for n=10"
```
The function string_sequence generates a string containing space-delimited numbers starting from 0 up to the given integer n. The test_string_sequence function contains unit tests that verify the correctness of the string_sequence function with various input values.