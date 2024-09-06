```python
def greatest_common_divisor(a, b):
    if b == 0:
        return a
    return greatest_common_divisor(b, a % b)
```
This GCD algorithm is a specialization of the Euclidean algorithm that calculates the GCD of two numbers by repeatedly replacing the larger number by the smaller number divided by the remainder of the division of the larger number by the smaller number. This continues until the remainder is zero, at which point the smaller number is the GCD of the two original numbers. It is called "self-contained" because it does not rely on any external libraries or modules to work, unlike the Python built-in `math.gcd` function. 
The function includes an initial check for when `b` is zero, which prevents an infinite loop in the algorithm and directly returns `a` as the GCD since `b` plays no role in the GCD of `a` and `0`. 

This algorithm is known for its efficiency, as it requires only a constant amount of storage space, making it suitable for computing the GCD of very large numbers. It is often used as an optimization technique in various applications, such as calculating the GCD of two numbers with a large difference in value.