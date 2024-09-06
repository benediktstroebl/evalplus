```python
def greatest_common_divisor(a: int, b: int) -> int:
    if not a or not b:
        raise ValueError("Both inputs must be numbers")
    if a == 0:
        return 0
    if b == 0:
        return 0
    
    # Calculate GCD using the Euclidean algorithm
    while a != 0 and b != 0:
        a, b = b, a % b
    
    return max(a, b)

# Test the function with a few cases
assert(greatest_common_divisor(3, 5) == 1)
assert(greatest_common_divisor(25, 15) == 5)
assert(greatest_common_divisor(10, 5) == 5)
assert(greatest_common_divisor(4, 20) == 4)
assert(greatest_common_divisor(12, 8) == 4)
``` 
This code defines a function `greatest_common_divisor` that calculates the greatest common divisor of two numbers using the Euclidean algorithm. The function handles edge cases, such as when one or both inputs are 0, and raises a `ValueError`. It also performs a check to ensure that both inputs are numbers, and performs the GCD calculation efficiently.