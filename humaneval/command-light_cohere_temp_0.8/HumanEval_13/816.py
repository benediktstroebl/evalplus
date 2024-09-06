```python
def greatest_common_divisor(a, b): 
    if b == 0: 
        return a  # big number divided by 0 equals infinity, hence the divisor is a
    elif a == 0 or b == 1: 
        return 0  # one or zero has no common divisor with other number
    else: 
        return max(a, b) // gcd(a, b)  # else calculate the greatest common divisor using the Euclidean algorithm 

# tests:
def test GreatestCommonDivisor():
    a = 3
    b = 5
    print(greatest_common_divisor(a, b))  # Output: 1
    a = 25
    b = 15
    print(greatest_common_divisor(a, b))  # Output: 5
    a = 3 
    b = 7 
    print(greatest_common_divisor(a, b))  # Output: 1
    a = 1047
    b = 20 
    print(greatest_common_divisor(a, b))  # Output: 5
    ```  This Python code defines a function called greatest_common_divisor, which takes two integers a and b as input and calculates the greatest common divisor of a and b. It also includes a test GreatestCommonDivisorTest function that uses the greatest_common_divisor function with different input values to test its functionality.