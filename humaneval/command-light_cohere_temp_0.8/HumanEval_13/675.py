```python
def greatest_common_divisor(a, b):
    if not a or not b:
        return 0
    
    # since only even numbers are being considered for GCD, we need to check if both numbers are even
    if not (a % 2 == 0 and b % 2 == 0) or (a % 2 != 0 and b % 2 != 0):
        return 2
    
    # similar condition for odd numbers
    if a % 2 == 0 and b % 2 != 0:
        return 1
    
    # since one of the numbers is even and other is odd, we need to use the Euclidean algorithm
    gcd = a
    
    while b != 0:
        b, a = b, a % b
    
    return gcd

#test cases
print(greatest_common_divisor(3, 5))  # Output: 1
print(greatest_common_divisor(25, 15)))  # Output: 5
```