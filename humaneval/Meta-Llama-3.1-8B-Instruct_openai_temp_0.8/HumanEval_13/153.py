```python
def greatest_common_divisor(a: int, b: int) -> int:
    """
    Return a greatest common divisor of two integers a and b
    
    The function uses the Euclidean algorithm to find the greatest common divisor.
    
    :param a: The first integer
    :param b: The second integer
    :return: The greatest common divisor of a and b
    """
    while b:
        a, b = b, a % b
    return abs(a)


# Test cases
if __name__ == "__main__":
    print(greatest_common_divisor(3, 5))  
    print(greatest_common_divisor(25, 15))
    print(greatest_common_divisor(48, 18))
```

This script defines a function `greatest_common_divisor` that takes two integers `a` and `b` and returns their greatest common divisor. It uses the Euclidean algorithm to achieve this. The test cases at the end of the script demonstrate the function's usage and verify its correctness.