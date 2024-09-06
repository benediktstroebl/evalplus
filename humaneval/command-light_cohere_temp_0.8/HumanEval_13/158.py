```python
def greatest_common_divisor(a, b):
    if not a or not b:
        return 0

    c = 0
    while b > 0:
        if a % b == 0:
            c += 1
        a //= b
    return c

# Test the function with various cases
 assert greatest_common_divisor(3, 5) == 1
 assert greatest_common_divisor(25, 15) == 5
 assert greatest_common_divisor(125, 250) == 5
 assert greatest_common_divisor(600, 1200) == 5
 assert greatest_common_divisor(10, 40) == 2
 assert greatest_common_divisor(1, 7) == 1
 assert greatest_common_divisor(16, 4) == 4
```
This code defines a function called greatest_common_divisor, which calculates the greatest common divisor of two numbers a and b. The function iteratively divides a numerator a by the divisor b, and whenever a is a multiple of b, c is incremented. This process continues until b becomes 0, at which point a is the GCD of a and b. The code then tests the test cases to ensure the correctness of the function. 

Note that, this function computes the GCD of two numbers a and b, which is a fundamental mathematical operation with many applications, including prime factor identification and number theory.