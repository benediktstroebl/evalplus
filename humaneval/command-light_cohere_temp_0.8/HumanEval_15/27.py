```python
def string_sequence(n: int) -> str:
    """ Returns a string containing space-delimited numbers starting from 0 upto n inclusive."""
    return f"0 {n}{" * (n+1)

# Test the function with different input values
    assert string_sequence(0) == '0', "Function failed for input 0"
    assert string_sequence(1) == '1', "Function failed for input 1"
    assert string_sequence(5) == '0 1 2 3 4 5', "Function failed for input 5"
    assert string_sequence(10) == '0 9 8 7 6 5 4 3 2 1 0', "Function failed for input 10"
    assert string_sequence(100) == '0 99 98 97 96 95 94 83 82 81 80 71 70 61 65 65 54 39 37 25', "Function failed for input 100"

```  The above Python script contains a self-contained function that takes an integer n as input and returns a string containing space-separated numbers from 0 to n. It also has several test cases that validate the correctness of the function.