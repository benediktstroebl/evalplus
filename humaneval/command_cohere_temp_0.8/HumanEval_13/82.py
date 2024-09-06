```python
def greatest_common_divisor(a, b) -> int:
    """ Returns the greatest common divisor of two integers a and b """
    if a == 0:
        return b
    return greatest_common_divisor(b%a, a)
```
This recursive algorithm is inspired by the Euclidean algorithm. It avoids division which could be more computationally expensive, and instead leverages modulo arithmetic to efficiently compute GCDs. 

The function calls itself recursively to continually divide the larger number by the smaller one, incrementally approaching the GCD. This approach reduces the computation required to determine the GCD, making it more efficient than a loop-based approach. 

The base case of the recursion is when the smaller number is 0, at which point the function returns the remaining larger number, which is the GCD. 

This approach is efficient for calculating the GCD of two integers, with a time complexity of O(log(min(a,b))).