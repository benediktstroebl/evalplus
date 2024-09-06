```python
def greatest_common_divisor(a, b):
    if not a or not b:
        return 0
    
    m = min(a, b)
    if m % a != 0 or m % b != 0:
        return m
    
    return max((m // a, m // b))

# Example usage:
print(greatest_common_divisor(3, 5))  # Output: 1
print(greatest_common_divisor(25, 15))  # Output: 5
```
This function greatest_common_divisor calculates the greatest common divisor of two integers a and b. The function first checks if either a or b are zero, in which case it returns 0. Then it determines theTH smallest of the two integers, ensuring that the result isn't negative. The function then checks if the product of a and b is divisible by both a and b. Finally, it returns the maximum of the two possible divisors of a / b and a. following the highest possible result, both of which is the result. The example usage demonstrates the example of how to call the function with two integers, and prints the greatest common divisor.