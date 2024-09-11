### Greatest Common Divisor (GCD) Calculator

Below is a self-contained Python script that calculates the greatest common divisor of two integers using the Euclidean algorithm.

```python
def greatest_common_divisor(a: int, b: int) -> int:
    """Return the greatest common divisor of two integers a and b"""
    
    while b!= 0:
        # In each iteration, replace 'a' with 'b' and 'b' with the remainder of 'a' divided by 'b'
        a, b = b, a % b
    
    return abs(a)


# Example usage:
print(greatest_common_divisor(3, 5))   # Output: 1
print(greatest_common_divisor(25, 15)) # Output: 5
```

In this script, the `greatest_common_divisor` function uses a simple iterative approach based on the Euclidean algorithm to find the GCD of two integers. The algorithm replaces 'a' with 'b' and 'b' with the remainder of 'a' divided by 'b' until 'b' becomes zero. At that point, 'a' is the GCD. The `abs` function is used to return a positive GCD, regardless of the signs of the input numbers.