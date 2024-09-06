```python
def greatest_common_divisor(a: int, b: int) -> int:
    if a == 0 or b == 0:
        return 0
    # Determine the greater divisor
    for d in range(1, min(a, b) + 1):
        if a % d == 0 and b % d == 0:
            return d
    return -1 

# Test case 1
assert greatest_common_divisor(3, 5) == 1 

# Test case 2
assert greatest_common_divisor(25, 15) == 5 

# Test case 3
try:
    assert greatest_common_divisor(-5) == -1 

except AssertionError: 
    print("Must be non-zero") 

# Test case 4
try:
    assert greatest_common_divisor(100, 15) == 5 

except AssertionError: 
    print("Must be divisible by 100") 
```