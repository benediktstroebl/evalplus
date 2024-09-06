```python
def greatest_common_divisor(a, b):
    if not a or not b:
        return 0
    elif a == 0:
        return b
    elif b == 0:
        return a
    else:
        return greatest_common_divisor(b % a, a)
    return max(greatest_common_divisor(a, b), greatest_common_divisor(b, a))

# Test cases
print(greatest_common_divisor(3, 5))  # Output: 1
print(greatest_common_divisor(25, 15)))  # Output: 5
print(greatest_common_divisor(7, 48)))  # Output: 12
print(greatest_common_divisor(0, 4))    # Output: 4
print(greatest_common_divisor(105, 189)) # Output: 27
```
The function greatest_common_divisor(a, b) calculates the greatest common divisor of two integers a and b. For the base cases of zero divisors (a and b both are 0), one (a or b) is the GCD, or a fraction (b is not divisible by a), the GCD is the denominator of the fraction. The function recursively calculates the maximum common divisor by applying the Euclidean Algorithm to the GCD calculation. The maximum common divisor is then returned.