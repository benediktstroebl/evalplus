```python
def greatest_common_divisor(a: int, b: int) -> int:
    """
    Return a greatest common divisor of two integers a and b
    
    >>> greatest_common_divisor(3, 5)
    1
    >>> greatest_common_divisor(25, 15)
    5
    """
    while b!= 0:
        a, b = b, a % b
    return abs(a)


# Example use cases
if __name__ == "__main__":
    print(greatest_common_divisor(3, 5))  # Output: 1
    print(greatest_common_divisor(25, 15))  # Output: 5
    print(greatest_common_divisor(48, 18))  # Output: 6
```

This script defines a function `greatest_common_divisor(a, b)` that uses the Euclidean algorithm to calculate the greatest common divisor (GCD) of two integers `a` and `b`. The GCD of two numbers is the largest positive integer that divides both numbers without leaving a remainder. The function takes two integers as input, calculates the GCD using the Euclidean algorithm, and returns the result. The example use cases at the end of the script demonstrate the usage of the function with different inputs.