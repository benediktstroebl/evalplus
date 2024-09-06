```python
def greatest_common_divisor(a, b):
    if b == 0:
        return a
    return greatest_common_divisor(b, a % b)
```
The algorithm works by recursive subdivision of the problem into two subproblems: the first one is “find the GCD of a and b” and the second one is “find the GCD of b and a % b”. The recursion rolls back the modulus operation against b. 

The base case is when b is 0, at which point the function returns a. That's because the GCD of two numbers is the numerator of their division, and if we divide any number by 0, the result is undefined in mathematics. 

This approach is efficient due to the recursive nature of the algorithm. With each recursive call, the problem is split into smaller subproblems, and this subdivision continues until the base case is reached. The time complexity of the algorithm is O(log(min(a, b))).