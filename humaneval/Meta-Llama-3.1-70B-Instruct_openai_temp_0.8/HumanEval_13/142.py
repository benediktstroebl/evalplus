```python
def greatest_common_divisor(a: int, b: int) -> int:
    """
    Return a greatest common divisor of two integers a and b
    
    This function uses the Euclidean algorithm to find the GCD.
    The Euclidean algorithm is a method for finding the greatest common divisor of two numbers.
    It works by repeatedly dividing the larger number by the smaller number and taking the remainder.
    
    Args:
        a (int): The first integer
        b (int): The second integer
    
    Returns:
        int: The greatest common divisor of a and b
    """
    while b!= 0:
        # Store the remainder of a divided by b in a temporary variable
        temp = b
        # Update b to be the remainder of a divided by b
        b = a % b
        # Update a to be the previous value of b
        a = temp
    return a

# Test the function
print(greatest_common_divisor(3, 5))  # Expected output: 1
print(greatest_common_divisor(25, 15))  # Expected output: 5
```

This script defines a function `greatest_common_divisor` that calculates the greatest common divisor (GCD) of two integers using the Euclidean algorithm. The function takes two integers `a` and `b` as input and returns their GCD.

The script also includes two test cases to verify the correctness of the function. The first test case checks that the GCD of 3 and 5 is 1, and the second test case checks that the GCD of 25 and 15 is 5.