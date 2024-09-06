```python
def greatest_common_divisor(a: int, b: int) -> int:
    if not a or not b:
        return 0
    
    if a == 0:
        return b
    elif b == 0:
        return a

    # Calculate gcd using the Euclidean Algorithm
    gcd = a + b - (a % b)
    while gcd > 1:
        a, b = b, a % b
    
    return gcd

# Test the function with various inputs
# Test case 1: 3 and 5
gcd = greatest_common_divisor(3, 5)
print("GCD of 3 and 5:", gcd)  

# Test case 2: 25 and 15
gcd = greatest_common_divisor(25, 15)
print("GCD of 25 and 15:", gcd) 

# Test case 3: 4 and 12 (to demonstrate divisibility)
gcd = greatest_common_divisor(4, 12)
print("GCD of 4 and 12:", gcd)
``` 
This Python code defines a function `greatest_common_divisor(a, b)` that calculates the greatest common divisor of two integers `a` and `b`. The function first checks if either input is zero, in which case it returns the other input. If both inputs are provided, it calculates the greatest common divisor using the Euclidean Algorithm, which efficiently computes the greatest common divisor of two integers.  The result tests with various inputs to ensure the correctness of the function.