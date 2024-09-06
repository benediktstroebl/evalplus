```python
def greatest_common_divisor(a: int, b: int) -> int:
    if not a or not b:
        return 0

    # Find the GCD using the Euclidean algorithm
    while b:
        a, b = b, a % b

    return a

# Test cases
print(greatest_common_divisor(3, 5))  # Output: 1
print(greatest_common_divisor(25, 15)))  # Output: 5
``` 
This function calculates the greatest common divisor of two numbers a and b. Using the Euclidean algorithm, which efficiently computes the GCD of two integers. It handles cases where either or number is zero or is invalid, returning 0 in such cases.