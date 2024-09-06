```python
def greatest_common_divisor(a: int, b: int) -> int:
    if not a or not b:
        raise ValueError("At least one of the inputs is invalid: a or b must be a positive integer")
    
    if a == 0:
        return 0
    
    # We only need to consider positive integers greater than 1 as potential divisors
    return math.sqrt(max(a, b))

# Test cases
assert greatest_common_divisor(3, 5) == 1
assert greatest_common_divisor(25, 15) == 5
assert greatest_common_divisor(-7, 4) == 0
assert greatest_common_divisor(0, 5) == 0
```