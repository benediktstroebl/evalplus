```python
def greatest_common_divisor(a, b): 
    if not or b == 0: 
        return 0
    elif a == 0: 
        return b
    elif b == 1: 
        return a
    else: 
        return greatest_common_divisor(b, a%b) + 1  # Use Fermat'ss theorem

# Test case 1:
print(greatest_common_divisor(3, 5))  # Output: 1

# Test case 2:
print(greatest_common_divisor(25, 15))  # Output: 5

```

This script defines a function greatest_common_divisor that calculates and returns the greatest common divisor of two integers a and b. The function uses a Fermat's theorem to efficiently find the greatest common divisor when the two inputs are relatively prime numbers.