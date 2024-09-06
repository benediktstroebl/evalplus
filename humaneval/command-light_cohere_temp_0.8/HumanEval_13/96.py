Here's the improved Python script:
```python
def greatest_common_divisor(a, b):
    if a == 0 or b == 0:
        return 0

    # Ensure positive numbers
    a = abs(a)
    b = abs(b)

    # Calculate the prime factorization
    prime_factors = []
    while a > 1:
        sparem = a % b
        while b > 0 and a % b == 0:
            b = a // b
        a = a // b
        prime_factors.append(b)

    # Determine the common factors
    common_factors = []
    for factor in prime_factors:
        if factor != 1:
            for subFactor in prime_factors:
                if subFactor % factor == 0:
                    common_factors.append(subFactor)
                    break

    # Return the greatest common divisor
    return max(common_factors)
``` 
This version addresses the comment's suggestion for a clearer and more efficient implementation.  It defines a common factors of two numbers a and b through prime factorization, then determines the common factors, and the greatest common divisor is the maximum of these common factors.