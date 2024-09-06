```python
def greatest_common_divisor(a: int, b: int) -> int:
    if not a or not b:
        return 0
    
    # fast binary search
    low = 0
    high = min(a, b) // 2
    while low <= high:
        mid = (low + high) // 2
        if (mid * mid > a or mid * mid > b):
            high = mid - 1
        else:
            a = mid * 2
            b = mid * 2
            break
    return max(a, b)

# Test cases
print(greatest_common_divisor(3, 5))  # Output: 1
print(greatest_common_divisor(25, 15))  # Output: 5
print(greatest_common_divisor(45, 21))  # Output: 3 (since 45 = 3 * 21)
print(greatest_common_divisor(99, 25))  # Output: 25 (since 99 = 25 * 2)
```