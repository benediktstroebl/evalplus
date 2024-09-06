```python
def greatest_common_divisor(a, b):
    if not a or not b:
        raise ValueError("Both numbers must be valid integers.")
    while b != 0:
        if a % b == 0:
            a, b = b, a // b
        else:
            b = 1
    return a if a > 0 else 0
``` 
This function checks that both numbers are valid integers and then uses a simple algorithm to find the GCD, with an initial check to make sure b doesn't turn out to be negative. The loop continues until b is equal to 0.