```python
def greatest_common_divisor(a: int, b: int) -> int:
    """
    Return a greatest common divisor of two integers a and b

    This function uses the Euclidean algorithm to find the greatest common divisor.
    The Euclidean algorithm is a way of calculating the greatest common divisor of two numbers,
    a and b, by successively applying the remainder operation.

    Args:
        a (int): The first integer.
        b (int): The second integer.

    Returns:
        int: The greatest common divisor of a and b.
    """
    # Base case: if b is zero, the greatest common divisor is a
    if b == 0:
        return a
    else:
        # Recursive case: call the function with b and the remainder of a divided by b
        return greatest_common_divisor(b, a % b)


# Test cases
if __name__ == "__main__":
    print(greatest_common_divisor(3, 5))   # Expected output: 1
    print(greatest_common_divisor(25, 15)) # Expected output: 5
    print(greatest_common_divisor(48, 18)) # Expected output: 6
    print(greatest_common_divisor(101, 103)) # Expected output: 1
```

This script defines a function `greatest_common_divisor` that calculates the greatest common divisor of two integers using the Euclidean algorithm. It includes test cases to verify the correctness of the function.