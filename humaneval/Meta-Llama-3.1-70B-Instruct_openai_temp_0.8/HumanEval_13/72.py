```python
def greatest_common_divisor(a: int, b: int) -> int:
    """
    Return a greatest common divisor of two integers a and b

    This function uses the Euclidean algorithm to find the GCD of two numbers.
    """
    while b:
        a, b = b, a % b
    return a

# Test cases
if __name__ == "__main__":
    assert greatest_common_divisor(3, 5) == 1
    assert greatest_common_divisor(25, 15) == 5
    print("All test cases passed")
```
This script defines a `greatest_common_divisor` function that takes two integers as input and returns their greatest common divisor. The function uses the Euclidean algorithm to calculate the GCD. The test cases are included to verify the correctness of the function.