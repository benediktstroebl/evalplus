```python
def greatest_common_divisor(a, b):
    """ Returns the greatest common divisor of two integers a and b """
    if a == 0:
        return b
    return greatest_common_divisor(b%a, a)
```

This recursive approach to finding the greatest common divisor is very efficient and inherently faster than using loops, especially for larger values of 'a' and 'b'. It leverages the fundamental mathematical property that gcd(a, b) == gcd(b%a, a). The base case of gcd(a, 0) == a has been used to optimize the algorithm further. 

The greatest common divisor (gcd) of two numbers is the largest number that divides both numbers evenly (without a remainder). In other words, it is the largest common divisor of two numbers. For example, the gcd of 8 and 12 is 4, as we can divide both numbers by 4 without a remainder. 

This function recursively calculates the gcd using the modulus operator '%' and returns the gcd of a and b.  It reduces the problem to the simpler problem of finding the gcd of 'b%a' and 'a', recursively. 

The time complexity of this recursive approach is O(log(min(a,b))). 

This algorithm is part of the efficient 'Euclidean Algorithm' family of integer factorization algorithms. It is important to note that this algorithm assumes that the inputs are integers and that a and b are not equal to zero. If either of these conditions is not met, the function will return an error, as the gcd between nonequal non-integer values or zero, is not defined in this context.