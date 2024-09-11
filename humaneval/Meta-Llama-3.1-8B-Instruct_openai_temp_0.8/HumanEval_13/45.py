```python
def greatest_common_divisor(a: int, b: int) -> int:
    """ Return a greatest common divisor of two integers a and b """
    
    # Base case: If b is zero, the GCD is a
    if b == 0:
        return a
    
    # Recursive case: GCD of a and b is the same as GCD of b and the remainder of a divided by b
    else:
        return greatest_common_divisor(b, a % b)

# Test cases
print(greatest_common_divisor(3, 5))  # Expected output: 1
print(greatest_common_divisor(25, 15))  # Expected output: 5
```

However, this recursive solution can be inefficient for large inputs because of the repeated calculations. A more efficient solution would use the Euclidean algorithm, which is an iterative approach that avoids repeated calculations.

Here's an example of the Euclidean algorithm:

```python
def greatest_common_divisor(a: int, b: int) -> int:
    """ Return a greatest common divisor of two integers a and b """
    
    # Base case: If b is zero, the GCD is a
    while b!= 0:
        # Swap a and b
        a, b = b, a % b
    
    # At this point, b is 0, and a is the GCD
    return a

# Test cases
print(greatest_common_divisor(3, 5))  # Expected output: 1
print(greatest_common_divisor(25, 15))  # Expected output: 5
```

This solution has a time complexity of O(log min(a, b)), which is more efficient than the recursive solution.