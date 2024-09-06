```python
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def intersection(a, b):
    # Determine intersection
    x1, y1 = a
    x2, y2 = b
    if x1 > y2 or x2 > y1:
        return "NO"
    ans = max(x1, x2) - min(y1, y2)
    # Determine if intersection is prime
    if is_prime(ans):
        return "YES"
    else: 
        return "NO"
```

The approach uses a simple algorithm to determine intersection and test if the length is prime. 

The `is_prime` function uses a basic primality test algorithm for integers, checking all integers up to the square root of the number in question. 

The `intersection` function first determines the intersection between `a` and `b`, and then proceeds to test if the length of the intersection is prime. If the length is prime, it returns "YES"; otherwise, it returns "NO". 

The code should work correctly for the given problem statement.