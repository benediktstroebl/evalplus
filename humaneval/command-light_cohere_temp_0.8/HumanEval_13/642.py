Here's the self-contained Python function that solves the problem of finding the greatest common divisor of two integers:
```python
def greatest_common_divisor(a, b):
    if not a or not b:
        return 0
    return max(a, b) / __gcd__(a, b)

def __gcd__(a, b):
    while b:
        a, b = b, a % b
    return a

# Example usage:
a = 25
b = 15
print(greatest_common_divisor(a, b))  # Output: 5
```
This function greatest_common_divisor takes two integers a and b as input, calculates their greatest common divisor using the `__gcd__` helper function, and returns the result. It effectively handles thel cases where either a or b are missing, or the greatest common divisor is calculated successfully.