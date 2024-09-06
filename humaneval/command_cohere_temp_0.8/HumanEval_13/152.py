```python
def greatest_common_divisor(a, b) -> int:
    """ Returns the greatest common divisor of two integers a and b """
    if a == 0:
        return b
    if b == 0:
        return a
    return greatest_common_divisor(b%a, a)
```

The function uses the Euclidean algorithm for computing the GCD. It is expressed in terms of a recursive helper function `greatest_common_divisor(b%a, a)`. This helper function efficiently computes the GCD of the two numbers by repeatedly replacing the larger number with the smaller number modulo the difference between them, until the remainder is zero, at which point the answer is the remaining non-zero number. 

It is a reimplementation of the following code:
```python
def gcd(a, b):
    if not a:
        return b
    if not b:
        return a
    return gcd(b % a, a)
```
The code example and test cases are taken from the Wikipedia article on the Euclidean algorithm. The article also has detailed explanations of the mathematics behind the algorithm.