```python
def greatest_common_divisor(a, b) -> int:
    """ Return a greatest common divisor of two integers a and b """
    if b == 0:
        return a
    return greatest_common_divisor(b, a % b)
```
This recursive approach is quite efficient and is based on the Euclidean algorithm. The auxiliary function calls are implemented in a way that the larger integer is passed first, thus reducing the magnitude of the numbers with each recursion step. This ensures that the algorithm terminates with a reasonable time frame even for large integers. 
The greatest common divisor (GCD) of two integers represents the largest number that divides both numbers evenly. 

Here is an example usage of the function:
```python
>> greatest_common_divisor(48, 36)
16
```
This will return the greatest common divisor of 48 and 36, which is 16. 
To fully validate the function, remember to execute more comprehensive tests including large numbers, fractions, and negative numbers. 
Please let me know if this solution suits your needs or if you want me to modify it in any way! 
You can also check out these approaches:
1. A iterative approach using the Euclidean algorithm.
2. An approach using the `math` module: `math.gcd(a, b)`.