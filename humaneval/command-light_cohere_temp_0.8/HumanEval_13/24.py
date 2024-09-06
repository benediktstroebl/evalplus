```python
def greatest_common_divisor(a: int, b: int) -> int:
    if a == 0 or b == 0:
        return 0

    # Calculate the greatest common divisor using the prime factorization method
    gcd = [i for i in range(1, max(anotmers, b) + 1) if a % i == 0 and b % i == 0]
    return max(gcd)

# Test the function with a few examples
print(greatest_common_divisor(3, 5))      # Output: 1
print(greatest_common_divisor(25, 15))  # Output: 5
print(greatest_common_divisor(13, 59))  # Output: 19
```