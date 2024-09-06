```python
def greatest_common_divisor(a: int, b: int) -> int:
    if a == 0 or b == 0:
        return 0
    
    # The biggest divisor that divides both a and b without a remainder
    return max(a, b) // gcd(a, b)
    
def gcd(a: int, b: int) -> int:
    while b != 0:
        a, b = b, a % b
    return a
    
# Unit tests
def test_greatest_common_divisor():
    assert greatest_common_divisor(3, 5) == 1
    assert greatest_common_divisor(25, 15) == 5

# Example usage
test_greatest_common_divisor()
``` 
This code provides a self-contained function and test suite to solve the problem of finding the greatest common divisor of two numbers. 

Please note that this implementation uses the Euclidean Algorithm for finding the greatest common divisor.  The may also be interested to use the Euclidean Algorithm to find the greatest common divisor of larger numbers.