```python
def greatest_common_divisor(a, b):
    """Return the greatest common divisor of two integers a and b."""
    while b:
        a, b = b, a % b
    return a
```
This Python script defines a function named `greatest_common_divisor` that takes in two integers a and b as parameters. The function utilizes a while loop that continues until b is greater than 0. The loop swaps the values of a and b at the start of each iteration, and the modulus operator (%) calculates the remainder of the division of b by a. This loop iteratively divides b by a until b becomes 0, ensuring that a is initially divisible by b but additionally guarantees that a is the largest divisor of b that doesn't exceed b. 

The script ensures that the GCD is calculated accurately, and the result is returned, representing the largest common divisor of the input integers a and b.