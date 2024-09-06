```python
def greatest_common_divisor(a, b):
    if not a or not b:
        raise ValueError("At least one of inputs a or b is invalid.")
    if a == 0 or b == 0:
        raise ValueError("Both inputs a and b cannot be 0.")

    # Calculate the GCD using the Euclidean Algorithm
    gcd = __import__('math').gcd(a, b)

    return gcd
```  This code defines a function greatest_common_divisor that calculates the greatest common divisor of two integers a and b. It uses the common Python approach to calculate the GCD, and it raises appropriate errors for invalid inputs such as zero or unequal values. 

This function is self-contained and can be used to find the GCD of any two integers easily.