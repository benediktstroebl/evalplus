```python
def greatest_common_divisor(a: int, b: int) -> int:
    if not a or not b:
        raise ValueError("One or both inputs must be a positive integer")
    if a == 0 or b == 0:
        return 0
    
    # We only need to consider positive divisors for now
    # This is a change from the description, which had no limit on a or b
    # You can uncomment the following line if you want to find the greatest divisor of all integers
    # The GCD(0, n) = 0 for any n
    if a == 1 or b == 1:
        return 1
    
    return max(a, b) // 1
```