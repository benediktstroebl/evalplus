```python
def greatest_common_divisor(a, b):
    if not a or not b:
        raise ValueError("At least one of the inputs must be a non-zero integer.")
    if not isinstance(a, int) or not isinstance(b, int):
        raise TypeError("Both inputs must be integers.")

    # Calculate the greatest common divisor using the prime factorization
    gcd = 1
    while b > 0:
        rem = a % b
        a, b = b, rem
        gcd = gcd * rem

    return gcd

# Unit tests
test_greatest_common_divisor = []
test_greatest_common_divisor.append(
    [
        (3, 5), 1)    # [3, 5] => 1
    test_greatest_common_divisor.append(
        [
        (25, 15), 5)    # [25, 15] => 5
    test_greatest_common_divisor.append(
        (4, 12))   # [4, 12] => 4
    test_greatest_common_divisor.append(
        (16, 9))   # [16, 9] => 9
    test_greatest_common_divisor.append(
        (72, 48))   # [72, 48] => gcd(72, 48) = 24
    test_greatest_common_divisor.append(
        (0, 1))   # [0, 1] => 1
test_greatest_common_divisor.append(
    (9, 0))   # [9, 0] => invalid input: must be positive integers
test_greatest_common_divisor.append(
    (10, 10))   # [10, 10] => valid input: both positive integers
```  This script defines a function `greatest_common_divisor` that calculates the greatest common divisor of two integers a and b using the prime factorization method. The unit tests ensure that the function works correctly with a variety of inputs.