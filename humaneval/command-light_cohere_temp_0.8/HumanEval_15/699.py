```python
def string_sequence(n: int) -> str:
    """ Return a string containing space-delimited numbers starting from 0 upto n inclusive"""
    return f"0 {n} {n+1} {n+2} {n+3}..."

def test_sequence(test_case: int) -> None:
    actual_sequence = string_sequence(test_case)
    expected_sequence = str(test_case)
    if actual_sequence != expected_sequence:
        raise ValueError("Incorrect output.

# Test cases
test_sequence(6)
test_sequence(10)
```
The function generates a string containing space-separated numbers from 0 to n, where n is the parameter passed. 
The function tests with the test_case function, which takes an integer and passes it to the string_sequence function to generate a sequence of numbers up to the given integer.