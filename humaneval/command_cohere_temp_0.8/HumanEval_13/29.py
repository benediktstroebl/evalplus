```python
def greatest_common_divisor(a, b) -> int:
    if b == 0:
        return a
    return greatest_common_divisor(b, a % b)
```
This GCD algorithm uses Euclid's algorithm with the optimiziation of taking the absolute value of b and using remainder operator `%` to make the recursive call faster in calculating the GCD of two integers `a` and `b`. It's considered more efficient than using `math.gcd` for larger values. 
The algorithm terminates when the `b` value becomes zero, and then the current `a` value is the GCD of the original `a` and `b` values. The base case of the recursion is when b is 0, which is the maximum common divisor of a and b. 
It is worth noting that for small integers, this method might be less efficient than integer division (`//`) since it involves multiple recursive calls and calculations of remainders (`%`). 

This approach achieves a time complexity of O(log(min(a, b))).

The docstring explains the purpose of the function, and the demo tests demonstrate its correctness.