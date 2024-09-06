```python
def greatest_common_divisor(a, b):
    """ Returns the greatest common divisor of two integers a and b """
    if a == 0:
        return b
    return greatest_common_divisor(b%a, a)
```
This recursive approach to finding the greatest common divisor is very efficient and is based on the Euclidean algorithm. This algorithm defines a recursive approach to finding the GCD of two numbers `a` and `b` where `b` is divided by `a` and the remainder is again subjected to the same process to be divided by `a`. This continues until `b` is no longer divisible by `a` and the remainder becomes `0`. 
The above process is termed as the Euclidean Algorithm since it is specifically designed to find the GCD of two numbers and it hails from the field of number theory identified with the renowned mathematician Euclid. The algorithm has been termed as the most efficient one to find the GCD of two numbers and is popularly used across various domains that include computer science, mathematics, and engineering. GCD stands for the Greatest Common Divisor and refers to the largest positive integer that divides two given numbers, `a`, and `b`, without leaving any remainder. 

This approach is efficient because instead of iteratively calculating the GCD, it recursively calculates the remainder after each division, thereby reducing the calculation to a few simple steps. 

The time complexity of the algorithm is `O(log(min(a, b)))`, which makes it an efficient solution for finding the GCD of two numbers.

This approach solves the problem of finding the GCD efficiently and can be tested using the following tests:
```python
def test_gcd():
    """
    Tests the greatest_common_divisor function
    """
    assert greatest_common_divisor(3, 5) == 1
    assert greatest_common_divisor(25, 15) == 5
    assert greatest_common_divisor(0, 15) == 15
    assert greatest_common_divisor(10, 0) == 0
    assert greatest_common_divisor(63, 105) == 3
    assert greatest_common_divisor(121, 123) == 1
```

This approaches finds the GCD without the need for any imported libraries, unlike the more straightforward approach of using `math.gcd()`.