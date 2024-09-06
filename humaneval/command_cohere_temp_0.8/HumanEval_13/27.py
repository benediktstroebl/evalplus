```python
def greatest_common_divisor(a, b):
    """Returns the greatest common divisor of two integers a and b."""
    while b:
        a, b = b, a % b
    return a
```
This function takes two integers a and b as input, and it iteratively computes the modular arithmetic quotient of a and b, representing the remainder of a divided by b as a decimal value. This operation is performed until b is zero. The resulting a value, which is the remainder of the final division, represents the greatest common divisor of the initial a and b values. The function then returns this greatest common divisor. 
The GCD, also known as the greatest common divisor or highest common divisor, is the largest positive integer that divides both a and b evenly (without a remainder). It is a fundamental mathematical concept used in many areas, such as arithmetic, algebra, and number theory.
To understand why the provided function works, it is essential to recognize that the GCD represents the largest number that divides both a and b without leaving a remainder. As an example, consider the numbers 12 and 18. Their GCD is 6, as repeatedly dividing 12 and 18 by 6 results in a remainder of 0. However, dividing by 4 would never result in no remainder for either 12 or 18. This demonstrates the property that the GCD is unique to the largest divisor that can be evenly distributed amongst the two numbers. 
This approach aligns with the Euclidean algorithm, a prominent method for computing the GCD. The algorithm utilizes a succession of division operations, refining the estimate of the GCD with each iteration. In contrast, other methods may employ exponentiation or prime factorization, although the provided approach is simpler and more efficient.  specific approaches relating to exponentiation or prime factorization.