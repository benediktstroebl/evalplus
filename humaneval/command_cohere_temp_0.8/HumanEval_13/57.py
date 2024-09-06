```python
def greatest_common_divisor(a, b):
    if b == 0:
        return a
    return greatest_common_divisor(b, a % b)
```
This recursive approach is quite efficient and wastes no time calculating divisors of unnecessary numbers. The base case of this recursion is b == 0, which is the smallest number relative to which 'a' is always divisible. 

The approach is called Euclidean Algorithm, and it's a widely used and efficient algorithm for finding the GCD of two integers a and b. Its runtime is O(log(min(a,b))) making it a relatively efficient algorithm for finding the GCD.