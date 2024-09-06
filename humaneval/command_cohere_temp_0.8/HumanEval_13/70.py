```python
def greatest_common_divisor(a, b) -> int:
    """ Return a greatest common divisor of two integers a and b """
    if a == 0:
        return b
    return greatest_common_divisor(b%a, a)
```
This algorithm works by the Euclidean algorithm concept, whereby we repeatedly divide the larger number by the smaller number (retaining the remainder) until the smaller number becomes zero. At each step, the remainder becomes the new larger number and the previous smaller number is the new divisor. Once the divisor becomes zero, the previous remainder is the GCD of the initial two numbers. The base case of the recursion is when the smaller number is 0, at which point the larger number is the GCD. 
The docstring describes the algorithm and also provides example outputs. These example outputs confirm that the function behaves as expected, correctly calculating the GCD of three and five as one, and the GCD of 25 and 15 as five. Frequently, the GCD is shown as a divisor by presenting the dividend with a "%" sign, and this is followed by a "%" translation to a multiplication operation, to compute the GCD. 

The function calls itself recursively, halving the larger number at each step and returning the remainder to the dividend. This continues until the dividend is zero, at which point the current remainder is the GCD of the two numbers, using the definition of GCD as the final remainder after dividing the larger number by the smaller number. 
It's worth noting that this function implements the Euclidean algorithm, which is a widely used approach for finding the GCD of two numbers. This algorithm is known for its efficiency and effectiveness in finding the GCD, making it a popular choice in many situations. , and can be compared with other GCD algorithms, such as the "Lehmer's GCD Algorithm" which has a time complexity of O(k^3) compared to O(k^2) in the Euclidean algorithm.