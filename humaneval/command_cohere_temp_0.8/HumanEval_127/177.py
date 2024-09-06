```python
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def intersection(a, b):
    mi = max(a[1], b[1])
    ma = min(a[0], b[0])
    if ma > mi:
        return "NO"
    if is_prime(mi - ma + 1):
        return "YES"
    else:
        return "NO"
```

The approach uses a basic primality test for integers, checking for divisibility by all numbers from 2 to the square root of the integer. If no divisors are found, the function considers the number as prime. 

The `intersection` function calculates the maximum and minimum values of the intersection and then checks whether the size of the intersection is prime, using the `is_prime` function. 

It returns "YES" if the size is prime and "NO" otherwise, also returning "NO" if the intervals do not intersect. It achieves the needed clarity and modularity of code to solve the problem statement.