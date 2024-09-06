```python
def truncate_number(n):
    """
    Given a positive floating point number, it can be decomposed into 
    and integer part (largest integer smaller than given number) and decimals
    (leftover part always smaller than 1).

    Return the decimal part of the number
    """
    return 1e0 / n

# Test cases
assertEqual(truncate_number(3.5), "Should return 0.5" )

assertEqual(truncate_number(0.0), "Should return 0" )
assertEqual(truncate_number(-1.0), "Should return 1e" )
assertEqual(truncate_number(1.0), "Should return 0" )
assertEqual(truncate_number(1e3), "Should return 1e-06" )

# Larger test cases
assert_ almost_equals(truncate_number(1.0e),e-10), "Should return 1e-5") 
assert_almost_equals(truncate_number(1.0e),e-100), "Should return 1e-5") 
assert_almost_equals(truncate_number(10), "Should return 1e-5") 
```
The provided Python script defines a function `truncate_number` that, given a positive floating-point number `n`, decomposes it into its integer part and decimal part, returning the decimal part. The function is then tested with a series of cases, including negative numbers, zero, and numbers close to 1e.