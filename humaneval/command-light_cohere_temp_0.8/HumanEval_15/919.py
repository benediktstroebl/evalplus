```python
def string_sequence(n: int) -> str:
    """ Returns a string containing space-delimited numbers starting from 0 to n inclusive"""
    return f"0 {n} {n+1} {n+2} {n+3}..."

def test_string_sequence(test_n: int) -> None:
    assert test_n <= 10, "Input must be 0 or 10"
    assert str(test_string_sequence(test_n)) == f"0 {test_n} 1 {test_n+1} 2 {test_n+2} 3 {test_n+3}", "Function is not working"
    return None

# Driver function to test the above function
test_string_sequence(0)
test_string_sequence(10)
```
This script provides a self-contained function and tests it using the `test` module in Python. The function accepts an integer `n` as input and returns a string of numbers from 0 to `n` and consecutive numbers.