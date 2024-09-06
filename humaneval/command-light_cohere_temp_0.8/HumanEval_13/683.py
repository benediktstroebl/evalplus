```python
def greatest_common_divisor(a, b): 
    while b != 0: 
        a_root = a % b 
        b = b // a 
    return a_root 

# Test case 1: 
print(greatest_common_divisor(3, 5)) 

# Test case 2: 
print(greatest_common_divisor(25, 15)) 

# Test case 3: 
print(greatest_common_divisor(2, 50)) 

# Test case 4: 
print(greatest_common_divisor(10, 3)) 

# Test case 5: 
print(greatest_common_divisor(56, 112)) 
``` 
Greatest Common Divisor is a function that calculates the Greatest Common Divisor for two numbers.  This takes two numbers a input and always returns the smaller number as the GCD, since it is always calculated from smaller to larger number.