```python
def greatest_common_divisor(a, b):
    if not a or not b:
        return 0
    
    # Handle negative numbers and reduce to positive
    a = abs(a)
    b = abs(b)
    
    for c in range(1, min(a, b) + 1):
        if a % c == 0 and b % c == 0:
            return c
    
    return 0

# Test cases
# 1. 3 and 5
 The GCD is 1
# 2. The GCD is 2
# 4 and 12 

# Test case 10: The GCD is 10
```