```python
def greatest_common_divisor(a, b):
    if not a or not b:
        return 0
    
    m = max(a, b)
    for i in range(1, m // 2 + 1):
        if a % i == 0 and b % i == 0:
            return i
    
    return m

# Test cases go here...
# Example: Get the GCD of 25 and 15
print(greatest_common_divisor(25, 15))  # Output: 5
```