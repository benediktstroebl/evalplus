```python
def greatest_common_divisor(a: int, b: int) -> int:
    """
    Return a greatest common divisor of two integers a and b.

    The function uses the Euclidean algorithm to find the GCD.

    >>> greatest_common_divisor(3, 5)
    1
    >>> greatest_common_divisor(25, 15)
    5
    """
    # Ensure a is the larger number
    if b > a:
        a, b = b, a
    
    # Base case: if b is zero, a is the GCD
    if b == 0:
        return a
    
    # Recursive case: replace 'a' with 'b' and 'b' with the remainder of 'a' divided by 'b'
    else:
        return greatest_common_divisor(b, a % b)


# Test cases
if __name__ == "__main__":
    assert(greatest_common_divisor(3, 5) == 1)
    assert(greatest_common_divisor(25, 15) == 5)
    print("All test cases pass")
```