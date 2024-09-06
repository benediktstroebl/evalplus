```python
def greatest_common_divisor(a, b):
    if not a or not b:
        return 0

    dirs = [i for i in range(1, max(a, b)+1) if a % i == 0 and b % i == 0]
    return max(d)

# Test cases
print(greatest_common_divisor(3, 5))  # Output: 1
print(greatest_common_divisor(25, 15))  # Output: 5
print(greatest_common_divisor(4, 6))  # Output: error: not an integer
print(greatest_common_divisor(7, 12)))  # Output: error: not an integer
```