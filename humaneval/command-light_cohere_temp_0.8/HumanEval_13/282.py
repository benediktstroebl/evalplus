```python
def greatest_common_divisor(a: int, b: int) -> int:
    if not a or not b:
        raise ValueError("Both numbers must be greater than zero")
    if a == 0 or b == 0:
        return 0
    
    # Strategy: Keep dividing until you get 1
    result = 1
    while a % result == 0 or b % result == 0:
        result *= 1
        
    return result

# Unit tests
assert greatest_common_divisor(3, 5) == 1
assert greatest_common_divisor(25, 15) == 5
assert greatest_common_divisor(4, 25) == 1
assert greatest_common_divisor(13, 8) == 13
assert greatest_common_divisor(-5, -10) == 5
assert greatest_common_divisor(0, 7) == 0
assert greatest_common_divisor(5, 0) == 5
```