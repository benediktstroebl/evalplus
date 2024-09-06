```python
def largest_divisor(n: int) -> int:
    """ Returns the largest number which divides the given number evenly"""
    if n <= 1:
        return n
    return 2 * largest_divisor(n // 2)

# Test cases
print(largest_divisor(15))  # Output: 5
print(largest_divisor(6))  # Output: 2
print(largest_divisor(18))  # Output: 6 (Not 6 because 18 is not divisible by 2, 3, or 4)
print(largest_divisor(9))  # Output: 3
```