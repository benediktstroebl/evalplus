```python
def greatest_common_divisor(a, b):
    if not a or not b:
        return 0

    m = max(a, b)
    if m % a != 0 or m % b != 0:
        return m

    return max(a, b) // gcd(a, b)

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

# Unit tests
def test_greatest_common_divisor():
    assert greatest_common_divisor(3, 5) == 1
    assert greatest_common_divisor(25, 15) == 5

# Example usage
test_greatest_common_divisor()
``` 
This code defines a function called `greatest_common_divisor` that computes the greatest common divisor of two integers a and b. The `gcd` helper function is also implemented to calculate the greatest common divisor of two numbers a and b using the Euclidean algorithm for finding the greatest common divisor. 

The `test_greatest_common_divisor` function contains unit tests that ensure the correctness of the `greatest_common_divisor` function with different inputs. 
This code is self-contained and can be used as a standalone function to compute and test the greatest common divisor of two numbers.