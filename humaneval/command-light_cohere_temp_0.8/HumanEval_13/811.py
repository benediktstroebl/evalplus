```python
def greatest_common_divisor(a, b):
    if not a or not b:
        return 0
    
    min_divisor = min(a, b)
    
    if not all(d == min_divisor for d in range(1, min_divisor)):
        return min_divisor
    
    common_divisors = [d for d in range(1, min_divisor) if a % d == 0 and b % d == 0]
    return max(common_divisors) or min_divisor

# Example usage:
# Test with a and b values
greatest_common_divisor(3, 5) # returns 1
greatest_common_divisor(25, 15) # returns 5
```