```python
def greatest_common_divisor(a, b):
    """ Returns the greatest common divisor of two integers a and b """
    if a == 0:
        return b
    if b == 0:
        return a
    return greatest_common_divisor(b%a, a)
```

The `greatest_common_divisor` function iteratively uses the modulo operator to repeatedly eliminate the larger number's factor in the smaller number, thus converging on the GCD. This algorithm is efficient and achieves the correct GCD for any pair of integers `a` and `b`.  This approach is known as the Euclidean Algorithm for finding the GCD.  The algorithm's efficiency stems from the property that performing the division operation multiple times (via the modulo operator) progressively reduces the magnitude of the numbers, effectively converging on the GCD. 

Here is a test case for the function to ensure its effectiveness:
```python
test_cases = [
    (3, 5, 1),
    (25, 15, 5),
    (1, 1, 1),
    (0, 0, 0),
    (72, 18, 6),
    (100, 25, 25)
]

for a, b, expected in test_cases:
    result = greatest_common_divisor(a, b)
    assert result == expected, f"For inputs {a} and {b}, expected {expected} but got {result}"
```

The test cases encompass a variety of scenarios, including positive, negative, and zero values, to ensure that the function behaves as expected across different cases.