```python
def greatest_common_divisor(a, b):
    """ Returns the greatest common divisor of two integers a and b """
    if a == 0:
        return b
    if b == 0:
        return a
    return greatest_common_divisor(b%a, a)
```

The GCD function uses Euclidean algorithm whereby a descending chain of inequalities is formed:
```
a ≧  b > b mod a > 0
```

Ultimately, `a` becomes the GCD, and the inequalities signify that it is the largest positive integer that can divide both `a` and `b` without a remainder. This process is reiterated until `b` becomes zero. 

The base case of the recursive function is when `a` or `b` is zero. Returning the value `0` in these instances ensures that the function ultimately returns the GCD. 

Let's expand two examples to illustrate this algorithm:
```
1. greatest_common_divisor(12, 18):
    - 18 > 12 ️
      12 > 18 ️
      12 > 18 % 12 ️
      6 > 6 ️
      6 > 6 % 6 ️
        0 > 0 ️
    - GCD is 6 

2. greatest_common_divisor(45, 105):
      105 > 45 ️
      45 > 105 ️
      45 > 105 % 45 ️
       21 > 21 ️
      21 > 21 % 21 ️
        0 > 0 ️
    - GCD is 45 ️
```

This approach significantly reduces the number of recursive calls. In the first example, it takes only two iterations to determine the GCD of 12 and 18, despite the fact that the function was called four times. In the second example, the function is called three times to determine the GCD of 45 and 105, reaching the base case in one iteration. 

The Euclidean algorithm accelerates the computation of GCDs and reduces the number of recursive calls, making the function more efficient.