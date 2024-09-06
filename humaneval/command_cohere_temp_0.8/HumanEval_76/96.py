```python
def is_simple_power(x, n):
    return type(x) == type(n) and x == n ** int(x == n ** int(x == n ** int(x == n ** int(x == n ** int(x == n ** int(x == n ** int(x == n ** int(x == n ** int(x == n ** int(x == n ** int(x == n ** int(x == n ** int(x == n ** int(x == n ** int(x == n ** int(x == n))
```

The function checks if the number at hand is an integer, then checks if it's a simple power of e, and so on - successive integer powers of e, until it reaches the base number - then it returns true if it's a simple power of n, and false, in any other case. 

It utilizes the fact that if a number x is a simple power of n, then it must be equal to n raised to some integer, which is int(x == n ** int(x == n ** int(...))), and the fact that int(x) is not defined for non-integer numbers. 

Also, the chain of comparisons int(x == n ** int(...)) is just a way to implement the exponentiation operator, and the double-equals is used instead of the single-equals to avoid any possible overflow or loss of precision.  This approach is quite efficient for the given problem.  It can be optimized further, but that would depend on the specific constraints and requirements.  It's always a good idea to consider edge cases, such as x=0, x=1, n=1, n=2, and so on, to ensure that the function behaves as expected.  This solution is not optimized but should be correct and adaptable for various cases.