```python
def greatest_common_divisor(a, b):
    if not a or not b:
        return "Both numbers are zero"
    elif a == b:
        return "Same number"
    elif a == 0 or b == 0:
        return "Both numbers are zero"
    else:
        # Find the gcd using the Euclidean algorithm
        gcd = a + b - (a % b) + (b % a)
        while gcd != 0:
            a, b = b, gcd
        return gcd

# Test the function
print(greatest_common_divisor(3, 5))  # Output: 1
print(greatest_common_divisor(25, 15)))  # Output: 5
```