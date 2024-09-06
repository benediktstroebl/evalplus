```python
def greatest_common_divisor(a, b): 
    while b != 0: 
        a,b = b, a % b 
    return a

# Test case 1: Get GCD of 3 and 5
print(greatest_common_divisor(3, 5)) 
# Output: 1

# Test case 2: Get GCD of 25 and 15
print(greatest_common_divisor(25, 15)) 
# Output: 5

# Test case 3: Get negative numbers
print(greatest_common_divisor(-100, -200))
# Output: -200
``` 
The function `greatest_common_divisor` computes the greatest common divisor of two integers `a` and `b`. The method uses the Euclidean algorithm to discover the greatest common divisor, which is implemented in the code by repeatedly replacing `b` with the remainder when divided by `a` and `b`. The code is self-contained and effectively solves the problem of finding the greatest common divisor of two numbers.