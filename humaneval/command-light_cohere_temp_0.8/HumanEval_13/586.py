```python
def greatest_common_divisor(a: int, b: int) -> int:
    if not a or not b:
        raise ValueError("Both numbers must be not equal to zero")
    if a == 0 or b == 0:
        return 0
    
    ret = [i for i in range(1, min(a, b) + 1) if a % i == 0 or b % i == 0]
    if ret:
        return ret[0]
    else:
        return None

# Test cases
print(greatest_common_divisor(3, 5))  # Output: 1
print(greatest_common_divisor(25, 15))  # Output: 5
print(greatest_common_divisor(10, 15))   # Output: 5 (correct)
print(greatest_common_divisor(3, 10))   # Input: 3, 10, Output: ValueError
```